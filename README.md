# Herramientas de Redes con Python

Proyecto educativo con 8 ejercicios de Python para analizar redes, comprobar conexiones y conocer protocolos de comunicación.

## Índice
1. Requisitos
2. Descripción de los ejercicios
3. Ejecución
4. Autor

## 1. Requisitos

- **Sistema operativo:** Windows, Linux o macOS.
- **Python:** 3.10 o superior.
- **RAM:** 2 GB mínimo.
- **Conexión a Internet:** Para pruebas externas.
- **Dependencias:** Solo bibliotecas estándar de Python.

## 2. Descripción de los ejercicios

### Ejercicio 1. Cálculo de subred IPv4
**Archivo:** `e01_subred.py`

Permite ingresar una dirección IP en formato CIDR y calcular automáticamente la dirección de red, máscara, prefijo, broadcast y rango de hosts disponibles. Utiliza la biblioteca `ipaddress`.

### Ejercicio 2. Identificación de IP local
**Archivo:** `e02_ip_local.py`

Obtiene el nombre del equipo y su dirección IP local mediante la biblioteca `socket`. Utiliza un socket UDP para identificar la dirección de red del dispositivo.

### Ejercicio 3. Ping a un host
**Archivo:** `e03_ping.py`

Comprueba si un equipo o servidor responde a solicitudes de ping. Utiliza `subprocess` para ejecutar comandos del sistema y `platform` para identificar el sistema operativo.

### Ejercicio 4. Barrido de ping de una subred
**Archivo:** `e04_barrido.py`

Analiza las direcciones IP de una subred para identificar equipos que responden al ping. Utiliza `ThreadPoolExecutor` para realizar varias comprobaciones simultáneamente y acelerar el proceso.

### Ejercicio 5. Escáner de puertos TCP
**Archivo:** `e05_puertos.py`

Comprueba si determinados puertos TCP de un servidor están abiertos o cerrados. Utiliza la biblioteca `socket` para intentar conexiones e identificar servicios como HTTP, HTTPS, SSH y FTP.

### Ejercicio 6. Resolución de nombres DNS
**Archivo:** `e06_dns.py`

Convierte nombres de dominio en direcciones IP y mide el tiempo necesario para resolverlos. También intenta obtener el nombre asociado a una IP mediante resolución inversa.

### Ejercicio 7. Latencia TCP con estadísticas
**Archivo:** `e07_latencia_tcp.py`

Realiza varios intentos de conexión TCP a un servidor y calcula el tiempo mínimo, máximo, promedio y porcentaje de conexiones fallidas. Utiliza `socket`, `time` y `statistics`.

### Ejercicio 8. Estado HTTPS y vencimiento del certificado
**Archivo:** `e08_https_certificado.py`

Comprueba el estado HTTP de una página web, mide su tiempo de respuesta y consulta los días restantes hasta el vencimiento de su certificado TLS. Utiliza `urllib`, `ssl` y `socket`.

## 3. Ejecución

Instalar Python desde https://www.python.org/

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python e01_subred.py
```

Cambiar el nombre del archivo para ejecutar otro ejercicio.

**Ejemplo:**

```bash
python e05_puertos.py
```

Los ejercicios se ejecutan de manera independiente. Las pruebas de red deben realizarse únicamente sobre equipos propios o autorizados.

## 4. Autor

**Matias Ramirez**

Proyecto académico de redes informáticas con Python — 2026.
