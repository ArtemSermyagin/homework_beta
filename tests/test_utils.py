from unittest.mock import patch

from src.utils import read_json, get_transaction


@patch("builtins.open", create=True)
def test_read_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "test data"
    assert read_json("../data/operations.json") == []


def test_get_transaction():
    assert get_transaction(441945886) == 31957.58
