"""
    You are a khmmadkhm scientist and you decided to play with electron distribution among atom's shells. You know that basic idea of electron distribution is that electrons should fill a shell untill it's holding the maximum number of electrons.

    Rules:
        Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell).
        For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
        Electrons should fill the lowest level shell first.
        If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.
    
    Ex.:    
        atomicNumber(1); should return [1]
        atomicNumber(10); should return [2, 8]
        atomicNumber(11); should return [2, 8, 1]
        atomicNumber(47); should return [2, 8, 18, 19]
"""


def atomic_number(electrons):
    shells = [[]]
    remaining_electrons = electrons

    while remaining_electrons:
        if is_shell_filled(shells[-1], len(shells)):
            """Last shell is filled, need to create a new empty one."""
            shells.append([])

        s_idx = len(shells)
        shell = shells[-1]
        s_capacity = get_shell_capacity(s_idx)

        shell = min(remaining_electrons, s_capacity)
        shells[s_idx - 1] = shell
        remaining_electrons -= shell

    return shells


def get_shell_capacity(shell_idx: int) -> int:
    """
    Returns the electron capacity of the shell
    Shells can fit 2n^2 electrons, where n is the n-ith shell.
    """
    return 2 * shell_idx ** 2


def is_shell_filled(shell: list[int], shell_idx: int) -> bool:
    """Is the shell filled?"""
    return get_shell_capacity(shell_idx) == shell
