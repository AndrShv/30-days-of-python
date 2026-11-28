import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Сервер теплицы запущен.")
logging.warning("Датчик #3 показывает низкий заряд батареи!")
logging.error("Не удалось подключиться к базе данных!")


def calculate_metrics(data):
    result = data * 2
    breakpoint()
    return result