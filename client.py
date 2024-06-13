import socket

def iniciar_cliente():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion_servidor = ('127.0.0.1', 12345)
    client_socket.connect(direccion_servidor)
    
    print("Conectado.")

    mensaje = "Hola"
    client_socket.sendall(mensaje.encode())

    client_socket.close()

if __name__ == "__main__":
    iniciar_cliente()