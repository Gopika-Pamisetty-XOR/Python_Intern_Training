def percent_to_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("score must be a number")

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def average(scores):
    if len(scores) == 0:
        raise ValueError("no scores")

    for score in scores:
        if score < 0 or score > 100:
            raise ValueError("invalid score")

    return sum(scores) / len(scores)


def has_passed(score, pass_mark=50):
    return score >= pass_mark