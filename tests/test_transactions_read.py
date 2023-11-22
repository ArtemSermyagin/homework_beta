import unittest

import pandas as pd
from unittest.mock import patch

from settings import OPEN_TRANSACTIONS_CSV, OPEN_TRANSACTIONS_XLSX
from src.transactions_read import transactions_open, transactions_xlsx_open


def test_transactions_open():
    with unittest.mock.patch("csv.DictReader") as mock_csv_reader:
        mock_csv_reader.return_value = [{"id": "1", "name": "Artem"}]
        result = transactions_open(OPEN_TRANSACTIONS_CSV)
    assert result == [{"id": "1", "name": "Artem"}]


def test_transactions_xlsx_open():
    with unittest.mock.patch("src.transactions_read.pd.read_excel") as mock_read:
        mock_read.return_value = pd.DataFrame({"id": [1], "name": ["Artem"]})
        result = transactions_xlsx_open(OPEN_TRANSACTIONS_XLSX)
    assert result == [{"id": 1, "name": "Artem"}]