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
    return result_mask


def create_mask_check(number_check: str) -> str:
    """
    Маскируем номер счета
    :param number_check: номер счета
    :return: замаскированный номер счета
    """
    return "**" + number_check[-4:]

