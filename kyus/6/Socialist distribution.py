"""
    A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what and that is exactly what you are called to do using this kata (which, on a side note, was born out of the necessity to redistribute the width of divs into a given container).

    You will be given two parameters, population and minimum: your goal is to give to each one according to his own needs (which we assume to be equal to minimum for everyone, no matter what), taking from the richest (bigger numbers) first.

    For example, assuming a population [2,3,5,15,75] and 5 as a minimum, the expected result should be [5,5,5,15,70]. Let's punish those filthy capitalists, as we all know that being rich has to be somehow a fault and a shame!

    If you happen to have few people as the richest, just take from the ones with the lowest index (the closest to the left, in few words) in the array first, on a 1:1 based heroic proletarian redistribution, until everyone is satisfied.

    To clarify this rule, assuming a population [2,3,5,45,45] and 5 as minimum, the expected result should be [5,5,5,42,43].

    If you want to see it in steps, consider removing minimum from every member of the population, then iteratively (or recursively) adding 1 to the poorest while removing 1 from the richest. Pick the element most at left if more elements exist with the same level of minimal poverty, as they are certainly even more aligned with the party will than other poor people; similarly, it is ok to take from the richest one on the left first, so they can learn their lesson and be more kind, possibly giving more gifts to the inspectors of the State!

    In steps:

        [ 2, 3, 5,45,45] becomes
        [-3,-2, 0,40,40] that then becomes
        [-2,-2, 0,39,40] that then becomes
        [-1,-2, 0,39,39] that then becomes
        [-1,-1, 0,38,39] that then becomes
        [ 0,-1, 0,38,38] that then becomes
        [ 0, 0, 0,37,38] that then finally becomes (adding the minimum again, as no value is no longer under the poverty threshold
        [ 5, 5, 5,42,43]
    If giving minimum is unfeasable with the current resources (as it often comes to be the case in socialist communities...), for example if the above starting population had set a goal of giving anyone at least 30, just return an empty array [].
"""

"""
    TODO: The logic works but not as expected by the Kata (https://www.codewars.com/kata/58cfa5bd1c694fe474000146/train/python)
    TODO: Here I am giving the maximum amount that the richest can give to the poorest
    TODO: While in the Kata they do it in a weird way by first removing the minimum wage from everyone's networth and then increasing or decreasing everyone's networth by one.. ???
"""




from typing import List
class Person:
    def __init__(self, networth: int):
        self.networth = networth

    def give(self, other, amount: int) -> None:
        if self.networth < amount:
            raise ValueError(
                f"Giving amount '{amount}' larger than networth '{self.networth}'")
        self.networth -= amount
        other.networth += amount

    def __lt__(self, other) -> bool:
        return self.networth < other.networth

    def __eq__(self, other) -> bool:
        return self.networth == other.networth


class Population:
    def __init__(self, population: List[int], minimum_wage: int):
        self.peoples = []
        self.minimum_wage = minimum_wage

        for person in population:
            self.peoples.append(Person(person))

    def find_richest(self) -> Person:
        return self.peoples[self.peoples.index(max(self.peoples))]

    def find_poorest(self) -> Person:
        return self.peoples[self.peoples.index(min(self.peoples))]

    def to_dict(self) -> List[int]:
        return [person.networth for person in self.peoples]


def socialist_distribution(population: List[int], minimum: int):
    population = Population(population, minimum)
    return richest_gives_poorest(population)


def richest_gives_poorest(population: Population):
    poorest = population.find_poorest()
    if poorest.networth >= population.minimum_wage:

        return population.to_dict()

    richest = population.find_richest()
    can_give = richest.networth - population.minimum_wage

    if not can_give:
        return []

    amount_to_give = population.minimum_wage - poorest.networth

    richest.give(poorest, min(amount_to_give, can_give))
    return richest_gives_poorest(population)


def main():
    print(socialist_distribution(
        [2, 3, 5, 15, 75], 5), 'expected:', [5, 5, 5, 15, 70])
    print(socialist_distribution(
        [2, 3, 5, 15, 75], 20), 'expected:', [20, 20, 20, 20, 20])
    print(socialist_distribution([2, 3, 5, 45, 45],
          5), 'expected:', [5, 5, 5, 42, 43])
    print(socialist_distribution([2, 3, 5, 45, 45], 30), 'expected:', [])
    print(socialist_distribution(
        [24, 48, 22, 19, 37], 30), 'expected:', [30, 30, 30, 30, 30])
    # print(socialist_distribution(
    #     [34, 14, 43, 17, 50, 1, 40, 50, -6, 36, 7, 28, 30, 21, 49, 6, 30, 40, 15, 48, 14, 37, -4, 43, 20, 37, 16, 34, 34, 23, -4, 31, 28, 11, 32, 39, -8, 35, -5, 10], 20),
    #     '\nexpected:\n',
    #     [27, 20, 27, 20, 27, 20, 27, 28, 20, 28, 20, 28, 28, 21, 28, 20, 28, 28, 20, 28, 20, 28, 20, 28, 20, 28, 20, 28, 28, 23, 20, 28, 28, 20, 28, 28, 20, 28, 20, 20])


if __name__ == '__main__':
    main()
