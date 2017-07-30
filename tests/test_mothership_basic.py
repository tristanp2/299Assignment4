
import unittest
import threading
import socket

from mothership.base import MothershipServer
from workers.basic_worker import BasicUserParseWorker


class TestMothershipBasic(unittest.TestCase):
    def test_mother_connection(self):
        def conn_and_send():
            while True:
                try:
                    address = 'localhost'
                    port = 8080
                    addr = (address,port)
                    sock = socket.socket()
                    sock.connect(addr)
                    sock.send(''.encode())
                except:
                    pass

        mother = MotherShipServer()

        address = settings.MOTHERSHIP.get('host', 'localhost')
        port = settings.MOTHERSHIP.get('port', 8080)
        addr = (address,port)
        sock = socket.socket()

        test_t = threading.Thread(None, mother.run())
        test_t.daemon = True
        test_t.start()

    
    
