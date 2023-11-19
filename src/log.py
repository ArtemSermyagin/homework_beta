import logging

# logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
#                     format="%(asctime)s %(filename)s %(levelname)s %(message)s")

file_formatter_1 = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_formatter_2 = logging.Formatter()
file_handler_1 = logging.FileHandler('utils_log.log', "w")
file_handler_1.setFormatter(file_formatter_1)

file_handler_2 = logging.FileHandler('masks_log.log', "w")
file_handler_2.setFormatter(file_formatter_1)

logger_1 = logging.getLogger(__name__)
logger_2 = logging.getLogger(__name__)

logger_1.addHandler(file_handler_1)
logger_2.addHandler(file_handler_2)

logger_1.setLevel(logging.DEBUG)
logger_2.setLevel(logging.DEBUG)
