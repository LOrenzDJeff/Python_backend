package main

import (
	"encoding/json"
	"fmt"
	"net"
)

type Characteristic struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
	Rsrp      float64 `json:"rsrp"`
}

func main() {
	// Данные для отправки на Python сервер
	data := []Characteristic{
		{Latitude: 55.0134451, Longitude: 82.9505132, Rsrp: -72},
		{Latitude: 55.0134172, Longitude: 82.9502775, Rsrp: -73},
		{Latitude: 55.0133529, Longitude: 82.9500039, Rsrp: -74},
	}

	// Адрес Python сервера
	pythonServerAddress := "localhost:65432"

	// Соединяемся с сервером
	conn, err := net.Dial("tcp", pythonServerAddress)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer conn.Close()

	// Кодируем данные в JSON
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling data:", err)
		return
	}

	// Отправляем данные на сервер
	_, err = conn.Write(jsonData)
	if err != nil {
		fmt.Println("Error sending data to server:", err)
		return
	}

	fmt.Println("Data sent to Python server")
}
