"""Модуль для работы с животными."""

class Animal:
    """Класс для представления животного."""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        """Возвращает информацию о животном."""
        return f"Info: Name: {self.name}, Color: {self.color}"


class Fish(Animal):
    """Класс для представления рыбы."""
    def __init__(self, name, color, location):
        super().__init__(name, color)
        self.location = location

    def info(self):
        """Возвращает информацию о рыбе."""
        return f"{super().info()}, Location: {self.location}"


class Bird(Animal):
    """Класс для представления птицы."""
    def __init__(self, name, color, max_speed):
        super().__init__(name, color)
        self.max_speed = max_speed

    def info(self):
        """Возвращает информацию о птице."""
        return f"{super().info()}, Max Speed: {self.max_speed}"


class Insect(Animal):
    """Класс для представления насекомого."""
    def __init__(self, name, color, size, date_of_discovery):
        super().__init__(name, color)
        self.size = size
        self.date_of_discovery = date_of_discovery

    def info(self):
        """Возвращает информацию о насекомом."""
        return (f"{super().info()}, Size: {self.size}, "
                f"Date of Discovery: {self.date_of_discovery}")


FILENAME = 'data.txt'
with open(FILENAME, 'r', encoding='utf-8') as file:
    array_of_animal = []

    for line in file:
        if 'ADD' in line:
            parts = line.split()
            family = parts[1]
            name_of_animal = parts[2]
            OBJ = None

            if family == 'Bird':
                max_speed_of_animal = float(parts[4])  # Преобразуем в float
                OBJ = Bird(name=name_of_animal, color=parts[3], max_speed=max_speed_of_animal)

            elif family == 'Fish':
                OBJ = Fish(name=name_of_animal, color=parts[3], location=parts[4])

            elif family == 'Insect':
                size_of_insect = float(parts[4])  # Преобразуем в float
                OBJ = Insect(name=name_of_animal, color=parts[3], size=size_of_insect,
                              date_of_discovery=parts[5])

            array_of_animal.append(OBJ)

        elif 'REM' in line:
            name_to_remove = line.split()[1]
            array_of_animal = [OBJ for OBJ in array_of_animal if OBJ.name != name_to_remove]

        elif 'print' in line:
            for OBJ in array_of_animal:
                print(OBJ.info())
