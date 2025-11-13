import socket
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from common import HEARTBEAT_REQUEST, HEARTBEAT_RESPONSE, HEARTBEAT_SIZE

def enviar_heartbeat_request(sock: socket.socket) -> bool:
    try:
        sock.sendall(HEARTBEAT_REQUEST)
        return True
    
    
    
    except socket.error as e:
        print(f"Erro ao enviar Heartbeat: {e}")
        return False


def receber_heartbeat_response(sock: socket.socket) -> bool:
    try:
        response = sock.recv(HEARTBEAT_SIZE)

        return response == HEARTBEAT_RESPONSE



    except socket.timeout:
        return False

    except socket.error as e:
        print(f"Erro ao receber resposta de Heartbeat: {e}")
        return False