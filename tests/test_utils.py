from unittest.mock import patch

import pytest

from settings import OPEN_JSONS, OPEN_JSONS_TEST
from src.utils import read_json, get_transaction


def test_read_full_json():
    assert read_json(OPEN_JSONS_TEST) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch("builtins.open", create=True)
def test_read_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "test data"
    assert read_json(OPEN_JSONS) == []


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Открытие вклада",
                "to": "Счет 41421565395219882431",
            },
            48223.05,
        )
    ],
)
def test_get_transaction(n, expected_result):
    assert get_transaction(n) == expected_result


def test_raises():
    with pytest.raises(ValueError):
        get_transaction(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
