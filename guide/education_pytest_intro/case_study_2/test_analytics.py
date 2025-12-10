import analytics


def test_average_marks():
    assert analytics.average_marks([80, 90, 100]) == 90

def test_average_of_single_score():
    assert analytics.average_marks([50]) == 50

def test_average_when_empty_list_passed_return_zero():
    assert analytics.average_marks([]) == 0