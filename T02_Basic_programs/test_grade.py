# test_grade.py
import pytest
from grade import grade

@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),   # high score
        (90, "A"),   # boundary
        (80, "B"),
        (75, "B"),   # boundary
        (65, "C"),
        (60, "C"),   # boundary
        (45, "D"),
        (40, "D"),   # boundary
        (20, "F"),
        (0, "F"),    # boundary
    ]
)
def test_grade_valid_scores(score, expected):
    assert grade(score) == expected


def test_grade_invalid_low():
    with pytest.raises(ValueError):
        grade(-1)


def test_grade_invalid_high():
    with pytest.raises(ValueError):
        grade(101)