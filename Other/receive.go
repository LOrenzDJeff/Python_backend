package main

import (
	"encoding/json"
	"fmt"
	"net"
)

type Result struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

func main() {
	// Адрес и порт для ожидания ответа от Python сервера
	listenerAddress := ":65433"

	// Создаем сервер для получения ответа от Python
	listener, err := net.Listen("tcp", listenerAddress)
	if err != nil {
		fmt.Println("Error creating listener:", err)
		return
	}
	defer listener.Close()

	fmt.Println("Waiting for response from Python server...")

	conn, err := listener.Accept()
	if err != nil {
		fmt.Println("Error accepting connection:", err)
		return
	}
	defer conn.Close()

	// Получаем ответ от сервера
	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println("Error reading from server:", err)
		return
	}

	// Декодируем ответ
	var result Result
	err = json.Unmarshal(buffer[:n], &result)
	if err != nil {
		fmt.Println("Error unmarshaling response:", err)
		return
	}

	// Выводим результат
	fmt.Printf("Received result: Latitude = %.10f, Longitude = %.10f\n", result.Latitude, result.Longitude)
}
