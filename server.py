import socket

def iniciar_server_tcp():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion = ('', 12345)
    server_socket.bind(direccion)
    
    server_socket.listen(1)
    
    print("Servidor TCP iniciado.")
    
    conexion, cliente = server_socket.accept()
    print(f"Conexión TCP establecida desde {cliente}")
    
    datos = conexion.recv(1024)
    print("Datos TCP recibidos:", datos)

    conexion.close()

if __name__ == "__main__":
    iniciar_server_tcp()