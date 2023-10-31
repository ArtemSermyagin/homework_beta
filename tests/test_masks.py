from src.masks import create_mask_card, create_mask_check


def test_mask():
    assert create_mask_card("1596837868705199") == "1596 83** **** 5199"
    assert create_mask_check("11111111111111111111") == "**1111"
