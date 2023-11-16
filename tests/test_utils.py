from unittest.mock import patch

from src.utils import read_json, get_transaction


@patch("builtins.open", create=True)
def test_read_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "test data"
    assert read_json("../data/operations.json") == []


def test_get_transaction():
    assert get_transaction({
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }) == 48223.05
