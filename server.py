import socket

def iniciar_server_udp():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    direccion = ('', 12345)
    server_socket.bind(direccion)
    
    print("Servidor UDP iniciado.")
    
    while True:
        datos, direccion_cliente = server_socket.recvfrom(1024)
        print(f"Datos UDP recibidos de {direccion_cliente}: {datos.decode()}")

if __name__ == "__main__":
    iniciar_server_udp()