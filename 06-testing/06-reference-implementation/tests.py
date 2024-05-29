import pytest
from search import Student, linear_search, binary_search

@pytest.mark.parametrize("students, target_id, expected", [
    ([], 5, None),  # No students in the list
    ([Student(1)], 1, Student(1)),  # Single student in the list, matches target_id
    ([Student(1), Student(2), Student(3)], 2, Student(2)),  # Target_id in the middle
    ([Student(1), Student(2), Student(3)], 1, Student(1)),  # Target_id is the first student
    ([Student(1), Student(2), Student(3)], 3, Student(3)),  # Target_id is the last student
    ([Student(1), Student(3), Student(5)], 4, None),  # Target_id not in the list
    ([Student(1), Student(3), Student(5)], 2, None),  # Target_id not in the list
    ([Student(1), Student(2), Student(3)], 0, None),  # Target_id less than the smallest id
    ([Student(1), Student(2), Student(3)], 4, None)   # Target_id greater than the largest id
])
def test_search_functions(students, target_id, expected):
    # Use linear search to find expected result
    assert linear_search(students, target_id) == expected
    # Use binary search to find expected result
    assert binary_search(students, target_id) == expected

    # Ensure both algorithms give the same result
    assert linear_search(students, target_id) == binary_search(students, target_id)
