package main

import (
	"encoding/json"
	"fmt"
	"net"
)

type Point struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
	Rsrp      int     `json:"rsrp"`
}

type Response struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

func main() {
	conn, err := net.Dial("tcp", "localhost:65432")
	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}
	defer conn.Close()

	points := []Point{
		{Latitude: 55.0134451, Longitude: 82.9505132, Rsrp: -72},
		{Latitude: 55.0134172, Longitude: 82.9502775, Rsrp: -73},
		{Latitude: 55.0133529, Longitude: 82.9500039, Rsrp: -74},
	}

	data, err := json.Marshal(points)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	_, err = conn.Write(data)
	if err != nil {
		fmt.Println("Error writing to server:", err)
		return
	}

	// Receive response from server
	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println("Error reading from server:", err)
		return
	}

	var response Response
	err = json.Unmarshal(buffer[:n], &response)
	if err != nil {
		fmt.Println("Error unmarshaling JSON:", err)
		return
	}

	fmt.Println("Received response from server:", response)
}
