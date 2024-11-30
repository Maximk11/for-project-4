def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует длину между различными единицами измерения.

    :param value: Значение для конвертации
    :param from_unit: Исходная единица измерения
    :param to_unit: Целевая единица измерения
    :return: Конвертированное значение
    """
    units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]


def convert_area(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует площадь между различными единицами измерения.

    :param value: Значение для конвертации
    :param from_unit: Исходная единица измерения
    :param to_unit: Целевая единица измерения
    :return: Конвертированное значение
    """
    units = {
        'm2': 1,
        'km2': 1e6,
        'cm2': 0.0001,
        'mm2': 1e-6,
        'acre': 4046.86,
        'mile2': 2.59e6,
        'ft2': 0.092903,
        'yd2': 0.836127
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_m2 = value * units[from_unit]
    return value_in_m2 / units[to_unit]


def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует объем между различными единицами измерения.

    :param value: Значение для конвертации
    :param from_unit: Исходная единица измерения
    :param to_unit: Целевая единица измерения
    :return: Конвертированное значение
    """
    units = {
        'm3': 1,
        'l': 1,
        'ml': 1e-3,
        'cm3': 1e-6,
        'ft3': 0.0283168,
        'in3': 1.63871e-5,
        'gal': 3.78541
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_m3 = value * units[from_unit]
    return value_in_m3 / units[to_unit]


def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует массу между различными единицами измерения.

    :param value: Значение для конвертации
    :param from_unit: Исходная единица измерения
    :param to_unit: Целевая единица измерения
    :return: Конвертированное значение
    """
    units = {
        'g': 1,
        'kg': 1000,
        'mg': 0.001,
        'lb': 453.592,
        'oz': 28.3495
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_grams = value * units[from_unit]
    return value_in_grams / units[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует температуру между различными единицами измерения.

    :param value: Значение температуры
    :param from_unit: Исходная единица измерения (C, F, K)
    :param to_unit: Целевая единица измерения (C, F, K)
    :return: Конвертированное значение температуры
    """
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9 / 5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5 / 9
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9 / 5 + 32
    else:
        raise ValueError(f"Невозможно конвертировать {from_unit} в {to_unit}")


def convert_time(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует время между различными единицами измерения.

    :param value: Значение времени
    :param from_unit: Исходная единица измерения (секунды, минуты, часы, дни)
    :param to_unit: Целевая единица измерения (секунды, минуты, часы, дни)
    :return: Конвертированное значение времени
    """
    units = {
        's': 1,
        'min': 60,
        'h': 3600,
        'd': 86400
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_seconds = value * units[from_unit]
    return value_in_seconds / units[to_unit]


def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует скорость между различными единицами измерения.

    :param value: Значение скорости
    :param from_unit: Исходная единица измерения (м/с, км/ч, миля/ч, фут/с)
    :param to_unit: Целевая единица измерения (м/с, км/ч, миля/ч, фут/с)
    :return: Конвертированное значение скорости
    """
    units = {
        'm/s': 1,
        'km/h': 1000 / 3600,
        'mile/h': 1609.34 / 3600,
        'ft/s': 0.3048
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Неизвестные единицы измерения: {from_unit}, {to_unit}")

    value_in_mps = value * units[from_unit]
    return value_in_mps / units[to_unit]


def main():
    """
    Главная функция для запуска конвертера единиц измерения.

    Пользователь выбирает категорию, вводит значение и выбирает исходные и целевые единицы измерения.
    Функция выводит результат конвертации.
    """
    print("Конвертер единиц измерения")

    category = input("Выберите категорию (length, area, volume, mass, temperature, time, speed): ").lower()

    value = float(input("Введите значение для конвертации: "))
    from_unit = input("Введите исходную единицу измерения: ").lower()
    to_unit = input("Введите целевую единицу измерения: ").lower()

    try:
        if category == 'length':
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'area':
            result = convert_area(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'volume':
            result = convert_volume(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'mass':
            result = convert_mass(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'time':
            result = convert_time(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        elif category == 'speed':
            result = convert_speed(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        else:
            print("Неверная категория.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()