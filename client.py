import socket

def iniciar_cliente_tcp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion_servidor = ('127.0.0.1', 12345)
    client_socket.connect(direccion_servidor)
    
    print("Conectado a servidor TCP.")

    mensaje = "Hola, servidor TCP"
    client_socket.sendall(mensaje.encode())

    client_socket.close()

if __name__ == "__main__":
    iniciar_cliente_tcp()