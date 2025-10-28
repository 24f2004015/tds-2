import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests an empty list."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Tests a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Tests a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks():
    """Tests multiple streaks and returns the longest."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 1, 2]) == 3
    assert longest_positive_streak([1, 2, 3, 0, 1, 2, 0, 4, 5, 6, 7]) == 4

def test_streaks_with_negatives():
    """Tests streaks broken by negative numbers."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3

def test_streak_at_beginning():
    """Tests a streak at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, -1, 5]) == 3

def test_streak_at_end():
    """Tests a streak at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4