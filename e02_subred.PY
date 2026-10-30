import socket

def ip_local():
    try:
        # Crear un socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Conectar al destino sin enviar datos
        s.connect(("8.8.8.8", 80))

        # Obtener la IP local
        ip = s.getsockname()[0]

        # Cerrar el socket
        s.close()

        return ip

    except OSError:
        return "127.0.0.1"


nombre = socket.gethostname()

print("Equipo:", nombre) 
print("IP local:", ip_local())