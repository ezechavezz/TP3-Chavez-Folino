import socket

def iniciar_cliente():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion_servidor = ('127.0.0.1', 12345)
    socket.connect(direccion_servidor)
    
    print("Conectado.")

    mensaje = "Hola"
    socket.sendall(mensaje.encode())

    socket.close()

if __name__ == "__main__":
    iniciar_cliente()