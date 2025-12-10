import pytest
from models import Student

@pytest.fixture
def sample_student():
    return Student(name='Alice', marks=[60, 70, 80])

def test_average(sample_student):
        assert sample_student.average() == (60 + 70 + 80)/3

def test_has_passed(sample_student):
      assert sample_student.has_passed() is True

def test_add_marks_changes_average(sample_student):
      old_average = sample_student.average()
      sample_student.add_mark(90)
      assert sample_student.average() != old_average