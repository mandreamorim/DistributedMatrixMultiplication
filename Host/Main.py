import socket
import time

from Utils import enviar_heartbeat_request, receber_heartbeat_response

def verificar_status_servidor(ip: str, port: int, timeout: float = 0.5) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))

            if not enviar_heartbeat_request(s):
                return False

            if receber_heartbeat_response(s):
                print(f"Servidor {ip}:{port} está ativo.")
                return True

            return False

    except (socket.timeout, ConnectionRefusedError, socket.error):
        return False
    except Exception as e:
        print(f"Erro inesperado ao verificar {ip}:{port}: {e}")
        return False


if __name__ == '__main__':
    SERVERS = [
        ('100.101.149.9', 65432),
    ]

    start_time = time.time()

    servidores_ativos = []
    for ip, port in SERVERS:
        if verificar_status_servidor(ip, port):
            servidores_ativos.append(ip)

    end_time = time.time()

    print("-" * 30)
    print(f"Verificação concluída em {end_time - start_time:.5f} segundos.")
    print(f"Servidores prontos para o cálculo: {servidores_ativos}")