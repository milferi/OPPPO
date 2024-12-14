import unittest
from io import StringIO
import sys
from main import Animal, Fish, Bird, Insect  

class TestAnimalClasses(unittest.TestCase):

    def test_animal_info(self):
        animal = Animal("Lion", "Yellow")
        self.assertEqual(animal.info(), "Info: Name: Lion, Color: Yellow")

    def test_fish_info(self):
        fish = Fish("Goldfish", "Orange", "Aquarium")
        self.assertEqual(fish.info(), "Info: Name: Goldfish, Color: Orange, Location: Aquarium")

    def test_bird_info(self):
        bird = Bird("Sparrow", "Brown", 15.5)
        self.assertEqual(bird.info(), "Info: Name: Sparrow, Color: Brown, Max Speed: 15.5")

    def test_insect_info(self):
        insect = Insect("Butterfly", "Yellow", 0.5, "2021-05-01")
        self.assertEqual(insect.info(), "Info: Name: Butterfly, Color: Yellow, Size: 0.5, Date of Discovery: 2021-05-01")

class TestCommandHandling(unittest.TestCase):

    def test_add_fish(self):
        animals = []
        family = 'Fish'
        name_of_animal = 'Goldfish'
        color_of_animal = 'Orange'
        location_of_animal = 'Aquarium'
        
        # Создаем объект Fish и добавляем его в список
        fish = Fish(name=name_of_animal, color=color_of_animal, location=location_of_animal)
        animals.append(fish)

        self.assertEqual(len(animals), 1)
        self.assertIsInstance(animals[0], Fish)

    def test_add_bird(self):
        animals = []
        family = 'Bird'
        name_of_animal = 'Sparrow'
        color_of_animal = 'Brown'
        max_speed_of_animal = 15.5
        
        # Создаем объект Bird и добавляем его в список
        bird = Bird(name=name_of_animal, color=color_of_animal, max_speed=max_speed_of_animal)
        animals.append(bird)

        self.assertEqual(len(animals), 1)
        self.assertIsInstance(animals[0], Bird)

    def test_remove_animal(self):
        animals = [Fish("Goldfish", "Orange", "Aquarium"), Bird("Sparrow", "Brown", 15.5)]
        
        # Удаляем Goldfish
        name_to_remove = "Goldfish"
        animals = [obj for obj in animals if obj.name != name_to_remove]

        self.assertEqual(len(animals), 1)
        self.assertEqual(animals[0].name, "Sparrow")

    def test_print_animals(self):
        animals = [Fish("Goldfish", "Orange", "Aquarium"), Bird("Sparrow", "Brown", 15.5)]
        
        # Переопределяем стандартный вывод
        captured_output = StringIO()
        sys.stdout = captured_output
        
        for obj in animals:
            print(obj.info())
        
        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__
        
        expected_output = (
            "Info: Name: Goldfish, Color: Orange, Location: Aquarium\n"
            "Info: Name: Sparrow, Color: Brown, Max Speed: 15.5\n"
        )
        
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
