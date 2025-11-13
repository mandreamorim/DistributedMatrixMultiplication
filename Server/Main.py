import os
import socket
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from common import HEARTBEAT_REQUEST, HEARTBEAT_RESPONSE, HEARTBEAT_SIZE

HOST = '0.0.0.0'
PORT = 65432


def handle_client(conn: socket.socket, addr: tuple):
    try:
        initial_data = conn.recv(HEARTBEAT_SIZE)

        if initial_data == HEARTBEAT_REQUEST:
            conn.sendall(HEARTBEAT_RESPONSE)
            print(f"Heartbeat respondido para {addr}")
            return

        elif initial_data:
            print(f"Recebida Tarefa de Matriz de {addr}. (Cálculo virá aqui...)")
            # ----------------------------------------------------
            # # LÓGICA FUTURA DE CÁLCULO E RESPOSTA DA MATRIZ
            # ----------------------------------------------------

        # else: (Conexão fechada sem dados)

    except Exception as e:
        print(f"Erro na conexão com {addr}: {e}")
    finally:
        conn.close()


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)  # Número máximo de conexões em fila
        print(f"Servidor de cálculo ouvindo em {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            # Idealmente, usaríamos um thread/processo para handle_client
            # Mas para simplicidade inicial, chamaremos diretamente
            handle_client(conn, addr)


if __name__ == '__main__':
    run_server()