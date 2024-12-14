package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Интерфейс Animal
type Animal interface {
	Info() string
}

// Структура для рыб
type Fish struct {
	Name     string
	Color    string
	Location string
}

// Реализация метода Info для Fish
func (f Fish) Info() string {
	return fmt.Sprintf("Fish: Name: %s, Color: %s, Location: %s", f.Name, f.Color, f.Location)
}

// Структура для птиц
type Bird struct {
	Name     string
	Color    string
	MaxSpeed float64
}

// Реализация метода Info для Bird
func (b Bird) Info() string {
	return fmt.Sprintf("Bird: Name: %s, Color: %s, Max Speed: %.2f", b.Name, b.Color, b.MaxSpeed)
}

// Структура для насекомых
type Insect struct {
	Name            string
	Color           string
	Size            float64
	DateOfDiscovery string
}

// Реализация метода Info для Insect
func (i Insect) Info() string {
	return fmt.Sprintf("Insect: Name: %s, Color: %s, Size: %.2f, Date of Discovery: %s", i.Name, i.Color, i.Size, i.DateOfDiscovery)
}

func main() {
	filename := "data.txt"
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var animals []Animal // Контейнер для хранения животных

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, "ADD") {
			handleAddCommand(line[4:], &animals) // Передаем строку после ADD и указатель на контейнер

		} else if strings.HasPrefix(line, "REM") {
			handleRemoveCommand(line[4:], &animals)

		} else if line == "PRINT" {
			printAnimals(animals)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
}

// Функция обработки команды ADD
func handleAddCommand(data string, animals *[]Animal) {
	parts := strings.Fields(data)
	if len(parts) < 3 {
		fmt.Println("Invalid ADD command format")
		return
	}

	objectType := parts[0]
	name := parts[1]
	color := parts[2]

	switch objectType {
	case "Fish":
		if len(parts) < 4 {
			fmt.Println("Invalid Fish data")
			return
		}
		location := parts[3]
		fish := Fish{Name: name, Color: color, Location: location}
		*animals = append(*animals, fish)

	case "Bird":
		if len(parts) < 4 {
			fmt.Println("Invalid Bird data")
			return
		}
		maxSpeed, err := strconv.ParseFloat(parts[3], 64)
		if err != nil {
			fmt.Println("Invalid Bird max speed")
			return
		}
		bird := Bird{Name: name, Color: color, MaxSpeed: maxSpeed}
		*animals = append(*animals, bird)

	case "Insect":
		if len(parts) < 5 {
			fmt.Println("Invalid Insect data")
			return
		}
		size, err := strconv.ParseFloat(parts[3], 64)
		if err != nil {
			fmt.Println("Invalid Insect size")
			return
		}
		dateOfDiscovery := parts[4]
		insect := Insect{Name: name, Color: color, Size: size, DateOfDiscovery: dateOfDiscovery}
		*animals = append(*animals, insect)

	default:
		fmt.Println("Unknown animal")
	}
}

// Функция обработки команды REM
func handleRemoveCommand(condition string, animals *[]Animal) {
	for i := len(*animals) - 1; i >= 0; i-- {
		animalInfo := (*animals)[i].Info()
		if strings.Contains(animalInfo, condition) {
			*animals = append((*animals)[:i], (*animals)[i+1:]...)
		}
	}
}

// Функция печати всех животных в контейнере
func printAnimals(animals []Animal) {
	for _, animal := range animals {
		fmt.Println(animal.Info())
	}
}
