from loop import count_to_five, countdown, sum_even_numbers

def test_count_to_five():
    assert count_to_five() == [1, 2, 3, 4, 5]

def test_countdown():
    assert countdown(3) == [3, 2, 1, 0]
    assert countdown(0) == [0]
    assert countdown(-1) == []

def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([1, 3, 5]) == 0
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([2, -4, 8]) == 6
