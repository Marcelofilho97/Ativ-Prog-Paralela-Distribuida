# importações
import threading
import socket

clients = []
def main():
    # Utilização do IPV4 e protocolo TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('localhost', 7777))
        server.listen() #para que o servidor esteja pronto para receber as conexões o "10" número de cnexões possíveis
    except:
        return print('\n não foi óssível iniciar o servidor \n')
    while True:
        #aceitar as conexões do clientes oriundas de seu endereço
        client, addr = server.accept()
        clients.append(client)

        #construção da thread
        thread = threading.Thread(target=msgTreatment, args={client})
        thread.start()
#Função responsável por "escutar" as mensagens de cada usuário
def msgTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break #para parar de receber mensagem desses clientes.
#Função de transmissão de mensagens para os outros usuários
def broadcast(msg, client):
    for IdClient in clients:
        if IdClient != client:
            try:
                IdClient.send(msg)
            except:
                deleteClient(IdClient)
#Função remover cliente se ele for desconectado
def deleteClient(client):
    clients.remove(client)

main()