import socket

def iniciar_cliente_udp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    direccion_servidor = ('127.0.0.1', 12345)
    
    print("Enviando mensaje a servidor UDP.")
    
    mensaje = "Hola, servidor UDP"
    client_socket.sendto(mensaje.encode(), direccion_servidor)

    client_socket.close()

if __name__ == "__main__":
    iniciar_cliente_udp()