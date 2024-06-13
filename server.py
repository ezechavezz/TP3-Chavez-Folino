import socket

def iniciar_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion = ('', 12345)
    server_socket.bind(direccion)
    
    server_socket.listen(1)
    
    print("Servidor iniciado.")
    
    conexion, cliente = server_socket.accept()
    print(f"Conexión establecida desde {cliente}")
    
    datos = conexion.recv(1024)
    print("Datos recibidos:", datos)

    conexion.close()

if __name__ == "__main__":
    iniciar_server()