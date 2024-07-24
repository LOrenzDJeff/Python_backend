import json
import socket

def from_go(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = b""
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet

            try:
                characteristics = json.loads(data.decode('utf-8'))
                print("Received characteristics:", characteristics)
                list_of_dicts = []
                for item in characteristics:
                    list_of_dicts.append([item['latitude'], item['longitude'], item['rsrp']])
                return list_of_dicts, addr
            except json.JSONDecodeError as e:
                print("Failed to decode JSON:", e)

def send_to_go(data, host='localhost', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        try:
            s.sendall(json.dumps(data).encode('utf-8'))
            print("Data sent to Go server:", data)
        except Exception as e:
            print("Failed to send data:", e)