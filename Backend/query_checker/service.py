import socket
import json
import main

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 7070))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  while True:
    data = conn.recv(4096)
    print(data.decode("utf-8").strip())
    if data.decode("utf-8").strip() == 'end':
      conn.close()
      break
    from_client = json.loads(data.decode('utf8'))
    vobj = main.QueryChecker(from_client,conn.getpeername())
    res = vobj.check()
    conn.send(f'{res}'.encode())