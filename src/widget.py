from src.masks import create_mask_card, create_mask_check


def print_type_data(type_data: str) -> str:
    """
    Маскирует данные карты и счета
    :param type_data:Информацией тип карты/счета и номер карты/счета
    :return: Возвращает эту строку с замаскированным номером карты/счета.
    """
    summ_data = type_data.split(" ")
    check = " ".join(summ_data[:-1])
    check_number = summ_data[-1]

    if len(check_number) == 16 and check.lower() != "счет":
        return f"{check.title()} {create_mask_card(check_number)}"
    elif len(check_number) > 16 and check.lower() == "счет":
        return f"{check.title()} {create_mask_check(check_number)}"
    else:
        return "Не верно введен номер счета или карты"


def format_date(date_time: str) -> str:
    """
    Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param date_time: "2018-07-11T02:26:18.671407"
    :return:"11.07.2018"
    """
    date = date_time.split("T")
    return ".".join(reversed(date[0].split("-")))


print(format_date("2018-07-11T02:26:18.671407"))
print(print_type_data("счет 15968378687051991"))

