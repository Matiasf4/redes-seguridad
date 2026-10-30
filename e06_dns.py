import socket
import time

nombre = input("Dominio a resolver: ").strip()
inicio = time.perf_counter()

try:
    canonico, alias, ips = socket.gethostbyname_ex(nombre)
except socket.gaierror:
    print("No se pudo resolver", nombre)
    raise SystemExit(1)

ms = (time.perf_counter() - inicio) * 1000

print("Nombre canonico:", canonico)

for ip in ips:
    print("IP:", ip)

print("Tiempo de resolucion: {:.1f} ms".format(ms))

try:
    print("Resolucion inversa:", socket.gethostbyaddr(ips[0])[0])
except socket.herror:
    print("Resolucion inversa: sin registro")