import score_to_grade
import pytest

@pytest.mark.parametrize(

    'score, expected',
    [
        (95, 'A'), 
        (80, 'A'), 
        (79, 'B'), 
        (65, 'B'), 
        (60, 'B'), 
        (59, 'C'), 
        (45, 'C'), 
        (40, 'C'), 
        (39, 'F'), 
        (10, 'F'), 
    ]
)

def test_grade_letter_ranges(score, expected):
    assert score_to_grade.convert_to_grade(score) == expected

@pytest.mark.parametrize('score', [-5, 105])
def test_grade_letter_invalid_scores(score):
    with pytest.raises(ValueError):
        score_to_grade.convert_to_grade(score)