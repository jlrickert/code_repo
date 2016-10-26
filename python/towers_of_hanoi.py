from itertools import chain


def identity(n):
    return n


def top(xs):
    if len(xs) > 0:
        return [xs[-1]]
    else:
        return []


def bottom(xs):
    if len(xs) > 0:
        return xs[:-1]
    else:
        return []


A = [5, 4, 3, 2, 1]
B = []
C = []


def move(n, source, target, auxiliary):
    """
    # >>> move(5, A, C, B)
    """
    if n > 0:
        # move n-1 disks from source to auxiliary, so they are out of the way
        move(n-1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '##############', sep='\n')

        # move the n-1 disks that we left on auxiliary onto target
        move(n-1, auxiliary, target, source)


def hanoi(n, a, b, c):
    """
    >>> hanoi(5, "a", "b", "c")
    [('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b'), ('c', 'a'), ('c', 'b'), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'a'), ('c', 'a'), ('b', 'c'), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b'), ('c', 'a'), ('c', 'b'), ('a', 'b'), ('c', 'a'), ('b', 'c'), ('b', 'a'), ('c', 'a'), ('c', 'b'), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b'), ('c', 'a'), ('c', 'b'), ('a', 'b')]
    """
    if n == 0:
        return []
    else:
        return hanoi(n-1, a, c, b) + [(a, b)] + hanoi(n-1, c, b, a)


def test_hanoi():
    expected = [
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'c'),
        ('a', 'b'),
        ('c', 'a'),
        ('c', 'b'),
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'c'),
        ('b', 'a'),
        ('c', 'a'),
        ('b', 'c'),
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'c'),
        ('a', 'b'),
        ('c', 'a'),
        ('c', 'b'),
        ('a', 'b'),
        ('c', 'a'),
        ('b', 'c'),
        ('b', 'a'),
        ('c', 'a'),
        ('c', 'b'),
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'c'),
        ('a', 'b'),
        ('c', 'a'),
        ('c', 'b'),
        ('a', 'b')
    ]

    answer = hanoi(5, "a", "b", "c")
    assert answer == expected
