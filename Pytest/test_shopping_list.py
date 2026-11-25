def test_shopping_list_length(shopping_list):
    assert len(shopping_list) == 3

def test_bread_in_shopping_list(shopping_list):
    assert "bread" in shopping_list

def test_chocolate_not_in_shopping_list(shopping_list):
    assert "chocolate" not in shopping_list
