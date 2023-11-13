import os
from datetime import datetime

from src.decorators import log


def test_log():
    filename = "test.txt"  # имя файла в который записывается log
    if os.path.exists(filename):  # Условие если по заданному пути есть файл,
        os.remove(filename)  # нужно удалить

    @log(filename)
    def func(x: int, y: int) -> float:
        return x / y

    now_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    func(1, 2)

    with open(filename) as file:  # Открываем файл для чтения логов
        log_mess = file.read().strip()  # читаем файл и удаляем с помощью
        # strip() не печатываемые символы в данном случае \n
    expected_log = f"{now_data} {func.__name__} ok"

    assert log_mess == expected_log


def test_log_err():
    filename = "test.txt"  # имя файла в который записывается log
    if os.path.exists(filename):  # Условие если по заданному пути есть файл,
        os.remove(filename)  # нужно удалить

    @log(filename)
    def func(x: int, y: int) -> float:
        return x / y

    now_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    func(1, 0)

    with open(filename) as file:  # Открываем файл для чтения логов
        log_mess = file.read().strip()  # читаем файл и удаляем с помощью
        # strip() не печатываемые символы в данном случае \n
    expected_log = f"{now_data} {func.__name__} error: division by zero, Inputs:(1, 0), {"{}"}"

    assert log_mess == expected_log


def test_console_log(capsys):
    @log()
    def func(x: int, y: int) -> float:
        return x / y

    now_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    func(1, 2)
    log_mess = capsys.readouterr()  # pytest.capsys.readouterr() заберет полученные данные из консоли
    expected_log = f"{now_data} {func.__name__} ok"

    assert log_mess.out.strip() == expected_log
