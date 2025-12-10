import pytest
from enrollment import count_passed

@pytest.fixture
def sample_enrollments():
    return [
        {'student' : 'Alice', 'course' : 'Math' , 'marks' : 75},
        {'student' : 'Bob', 'course' : 'Math' , 'marks' : 35},
        {'student' : 'Charlie', 'course' : 'Science' , 'marks' : 90},
        {'student' : 'Diana', 'course' : 'Math' , 'marks' : 50},
    ]

def test_count_passed_math(sample_enrollments):
    assert count_passed(sample_enrollments, 'Math') == 2

def test_count_passed_science(sample_enrollments):
    assert count_passed(sample_enrollments, 'Science') == 1

def test_count_passed_no_students(sample_enrollments):
    assert count_passed(sample_enrollments, 'History') == 0

def test_count_passed_with_higher_threshold(sample_enrollments):
    assert count_passed(sample_enrollments, 'Math', pass_threshold=50) == 2
