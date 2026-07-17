"""Разбор строк с полями вида ``key:value``.

Такой паттерн (обрезать пробелы -> разбить по разделителю полей ->
у каждого поля взять значение после ``:``) повторялся в нескольких
практических заданиях, поэтому вынесен в общую утилиту.
"""


def parse_kv_record(raw, field_sep, kv_sep=":"):
    """Превращает строку с полями ``key:value`` в словарь.

    Пример::

        parse_kv_record("  id:temp_01;val:23.5;status:active  ", ";")
        # -> {"id": "temp_01", "val": "23.5", "status": "active"}

    :param raw: исходная строка (лишние пробелы по краям обрезаются).
    :param field_sep: разделитель между полями (например ``";"`` или ``"_"``).
    :param kv_sep: разделитель между ключом и значением (по умолчанию ``":"``).
    :return: словарь ``{key: value}`` в порядке следования полей.
    """
    record = {}
    for field in raw.strip().split(field_sep):
        key, value = field.split(kv_sep, 1)
        record[key] = value
    return record
