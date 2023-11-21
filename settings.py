from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, "tests")
TEST_DECOR_PATH = Path.joinpath(DATA_PATH, "test_decorators.py")
TEST_GEN_PATH = Path.joinpath(DATA_PATH, "test_generators.py")
TEST_MASKS_PATH = Path.joinpath(DATA_PATH, "test_masks.py")
TEST_PEOCES_PATH = Path.joinpath(DATA_PATH, "test_processing.py")
TEST_UTILS_PATH = Path.joinpath(DATA_PATH, "test_utils.py")
TEST_WIDGET_PATH = Path.joinpath(DATA_PATH, "test_widget.py")
DATA_PATH_2 = Path.joinpath(ROOT_PATH, "data")
OPEN_JSONS = Path.joinpath(DATA_PATH_2, "operations.json")
OPEN_JSONS_TEST = Path.joinpath(DATA_PATH_2, "test_file.json")
OPEN_TRANSACTIONS_CSV = Path.joinpath(DATA_PATH_2, "transactions.csv")
OPEN_TRANSACTIONS_XLSX = Path.joinpath(DATA_PATH_2, "transactions_excel.xlsx")
