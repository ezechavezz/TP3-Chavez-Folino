import socket

def iniciar_cliente():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion = ('127.0.0.1', 12345)
    socket.connect(direccion)
    
    print("Cliente conectado al servidor.")

    mensaje = "Hola, servidor!"
    socket.sendall(mensaje.encode())

    socket.close()