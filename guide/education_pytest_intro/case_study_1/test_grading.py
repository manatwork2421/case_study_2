import grading

def test_is_pass_for_passing_score():
    grading.is_pass(80)

def test_is_pass_for_failing_score():
    grading.is_pass(30)