import socket

HEARTBEAT_REQUEST = b"HB_REQ"
HEARTBEAT_RESPONSE = b"HB_RESP"
HEARTBEAT_SIZE = len(HEARTBEAT_REQUEST)


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