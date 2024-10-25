# Método 1 - httpx
# import httpx
# result = httpx.get("http://example.com/index.html")
# print(result.status_code)
# print(result.headers)
# print(result.content)


# Método 2 - criando o próprio cliente
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))
cmd = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

client.close()


# Método 3 - urllib
# from urllib.request import urlopen
# result = urlopen("http://example.com/index.html")
# print(result.read())


# Método 4 - requests
# import requests
# result = requests.get("http://example.com/index.html")
# print(result.status_code)
# print(result.headers)
# print(result.content)
