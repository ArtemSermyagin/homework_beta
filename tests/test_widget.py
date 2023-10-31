import pytest

from src.widget import print_type_data


@pytest.fixture
def data():
    return "счет 159683"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa Classic 1596837868705199", "Visa Classic 1596 83** **** 5199"),
        ("счет 11111111111111111111", "Счет **1111"),
    ],
)
def test_data(string, expected_result):
    assert print_type_data(string) == expected_result


def test_data_assert(data):
    assert print_type_data("Visa Classic 1596837868705199") == "Visa Classic 1596 83** **** 5199"
    assert print_type_data("счет 11111111111111111111") == "Счет **1111"
    assert print_type_data("Visa Classic 12345678901234561") == "Не верно введен номер счета или карты"
    assert print_type_data(data) == "Не верно введен номер счета или карты"
