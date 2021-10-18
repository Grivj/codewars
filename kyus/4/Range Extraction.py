"""
    A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
    Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

    Example:

        solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
                 9, 10, 11, 14, 15, 17, 18, 19, 20])
        # returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

import unittest
from typing import List


def solution(args):
    rh = RangeHelper()
    return rh(args)


class RangeHelper:
    """
    Helper to turn a sequence in integers into a string,
    where integers are considered to be a range,
    when 2 or more elements are continuous. (ex: -3, -3, -1) -> (-3--1)
    """

    def __init__(self):
        self.sequence: List[int] = []
        self.current_sequence: List[int] = []
        self.sequences: List[List[int]] = []
        self.result: str = ""

    def __call__(self, sequence: List[int]):
        self.sequence = sequence
        self.make_sequences()
        self.make_result()
        return self.result

    def make_sequences(self):
        """
        Separates self.sequence into self.sequences,
        where self.sequences contains a list of continuous integers
        """
        for integer in self.sequence:
            if not self.current_sequence:
                self.current_sequence.append(integer)
                continue

            # is continuous
            if integer == self.current_sequence[-1] + 1:
                self.current_sequence.append(integer)
            else:
                # not continuous, push to sequences and clear current sequence
                self.sequences.append(
                    self.current_sequence)
                self.current_sequence = [integer]

        # push last current_sequence
        self.sequences.append(
            self.current_sequence)
        self.current_sequence = []

    def make_result(self):
        """
        Builds the string result from self.sequences.
        A continuous sequence with more than two members is shortened as such: [1-th]-[n-th],
        while sequences with 1 member simply returns it's member as a string.
        """
        for s_idx, sequence in enumerate(self.sequences):
            if len(sequence) > 2:
                self.result += str(sequence[0]) + '-' + str(sequence[-1])
            else:
                for i_idx, integer in enumerate(sequence):
                    self.result += str(integer)

                    if len(sequence) != 1 and i_idx != len(sequence) - 1:
                        self.result += ','

            if s_idx != len(self.sequences) - 1:
                self.result += ','
        self.result


class SolutionTest(unittest.TestCase):
    def basic_tests(self):
        self.assertEqual(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9,
                         10, 11, 14, 15, 17, 18, 19, 20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(
            solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), '-3--1,2,10,15,16,18-20')


def main():
    test = SolutionTest()
    test.basic_tests()


if __name__ == '__main__':
    main()
