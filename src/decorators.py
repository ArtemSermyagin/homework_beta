from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = "") -> Callable:
    """
    Получает аргументы, передаваемые в декоратор
    :param filename: имя файла для log
    :return: Callable
    """

    def wrapper(func: Callable) -> Callable:
        """
        Принимает в себя функцию
        :param func: функция которая задекорирована
        :return: Callable
        """

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """
            Inner получает аргументы из функции выше
            аргументы, передаваемые в функции при вызове
            :param args: Any
            :param kwargs: Any
            :return: Any
            """
            result = None
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_text = f"{date} {func.__name__} ok"
            except Exception as e:
                log_text = f"{date} {func.__name__} error: {e}, Inputs:{args}, {kwargs}"
            if filename:
                with open(filename, "a+") as file:
                    file.write(log_text + "\n")
            else:
                print(log_text)
            return result

        return inner

    return wrapper
