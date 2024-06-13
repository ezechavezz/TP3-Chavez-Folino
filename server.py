import socket

def iniciar():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion = ('', 12345)
    socket.bind(direccion)
    
    socket.listen(1)
    
    print("Servidor iniciado.")
    
    conexion, cliente = socket.accept()
    print(f"Conexión establecida desde {cliente}")
    
    datos = conexion.recv(1024)
    print("Datos recibidos:", datos)

    conexion.close()

if __name__ == "__main__":
    iniciar()