import unittest
import socket
import threading
import json
from network import from_go, send_to_go

class TestNetwork(unittest.TestCase):

    def setUp(self):
        self.server_thread = threading.Thread(target=self.mock_server, daemon=True)
        self.server_thread.start()
        self.host = 'localhost'
        self.port = 65432

    def mock_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data = b""
                while True:
                    packet = conn.recv(1024)
                    if not packet:
                        break
                    data += packet
                response = {"latitude": 55.010, "longitude": 82.946}
                conn.sendall(json.dumps(response).encode('utf-8'))

    def test_from_go(self):
        characteristics, addr = from_go(host=self.host, port=self.port)
        self.assertIsInstance(characteristics, list)
        self.assertEqual(addr[0], self.host)

    def test_send_to_go(self):
        data = {"latitude": 55.010, "longitude": 82.946}
        send_to_go(data, (self.host, self.port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(json.dumps(data).encode('utf-8'))
            response = s.recv(1024)
            response_data = json.loads(response.decode('utf-8'))
            self.assertEqual(response_data, data)

if __name__ == '__main__':
    unittest.main()
