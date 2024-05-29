from itertools import permutations
import pytest
from mergesort import split_in_two, merge_sorted, merge_sort

@pytest.mark.parametrize('ns', [
    list(range(n)) for n in range(101)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1


@pytest.mark.parametrize('left', [
    [], [1], [1, 2, 3], [4, 10, 15], [2, 5, 5, 9]
])
@pytest.mark.parametrize('right', [
    [], [1], [1, 2, 3], [4, 10, 15], [2, 5, 5, 9]
])
def test_merge_sorted(left, right):
    result = merge_sorted(left, right)
    assert result == sorted(left + right)


@pytest.mark.parametrize('expected, ns', [
    (sorted(list(perm)), list(perm)) for perm in permutations([1, 2, 3])
] + [
    (sorted(list(perm)), list(perm)) for perm in permutations([1, 1, 2, 2])
] + [
    (sorted(list(perm)), list(perm)) for perm in permutations([3, 2, 1])
] + [
    (sorted(list(perm)), list(perm)) for perm in permutations([1, 3, 2, 1])
] + [
    (sorted(list(perm)), list(perm)) for perm in permutations([5, 3, 8, 2])
] + [
    (sorted(list(perm)), list(perm)) for perm in permutations([4, 4, 4, 4])
])
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected