import socket

# data should be in json string format
# send as raw string 
# r'''<your json here>''''
'''
{
"og_query":"select key from users where username=x and passwd=x",
"input_vals":{"uname":"john","passwd":"1234"}
}
'''

def checkquery(data):
    server_ip = '127.0.0.1'
    port = 7070
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip,port))
    client.send(data.encode("utf-8"))
    response = client.recv(4096)
    response = response.decode("utf-8")
    client.send("end".encode('utf-8'))
    return response