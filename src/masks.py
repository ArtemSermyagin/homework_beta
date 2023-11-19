from src.log import logger_2


def create_mask_card(number: str) -> str:
    """
    Маскируем номер карты
    :param number: номер
    :return: замаскированный номер карты
    """
    number_list = list(number)
    index_symbol = [6, 7, 8, 9, 10, 11]
    for index in index_symbol:
        number_list[index] = "*"
    result = []
    for i in range(len(number)):
        result.append(number_list[i])
        if (i + 1) % 4 == 0:
            result.append(" ")
    result_mask = "".join(result)
    logger_2.info("Номер каты замаскирован")
    return result_mask[:-1]


def create_mask_check(number_check: str) -> str:
    """
    Маскируем номер счета
    :param number_check: номер счета
    :return: замаскированный номер счета
    """
    logger_2.info("Номер счета замаскирован")
    return "**" + number_check[-4:]


print(create_mask_card("1111111111111111"))
print(create_mask_check("1234567890123456789"))
