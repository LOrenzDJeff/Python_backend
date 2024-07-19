import socket
import json

def start_server(host='localhost', port=65432):
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
            
            # Decode and load JSON data
            try:
                characteristics = json.loads(data.decode('utf-8'))
                #print("Received characteristics:", characteristics)
                list_of_dicts = []
                for item in characteristics:
                    list_of_dicts.append([item['latitude'], item['longitude'], item['rsrp']])
                print(list_of_dicts)
            except json.JSONDecodeError as e:
                print("Failed to decode JSON:", e)

if __name__ == "__main__":
    start_server()
