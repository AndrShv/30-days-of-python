"""Небольшие статистические помощники."""


def average(values, default=0.0):
    """Безопасно считает среднее арифметическое.

    Возвращает ``default`` для пустой последовательности, что избавляет
    от повторяющейся проверки ``len(...) > 0`` перед делением.

    :param values: последовательность чисел.
    :param default: значение для пустой последовательности.
    :return: среднее значение или ``default``.
    """
    values = list(values)
    if not values:
        return default
    return sum(values) / len(values)
