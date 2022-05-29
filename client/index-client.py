# importações
import threading
import socket

def main():
    # Utilização do IPV4 e protocolo TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #Tentativa de conexão ao servidor
    try:
        client.connect(('localhost', 7777))
    except:
        return print('\n a conexão não foi possível com o servidor')
    #identificar o cliente através do seu USERNAME
    username = input('Usuário: \n')
    print('\n' + username + 'Está Conectado \n')
#criação das threads para que as funções implementadas funcionem ao mesmo tempo
    threadONE = threading.Thread(target=receiveMsg, args=[client])
    threadTWO = threading.Thread(target=sendMsg, args=[client, username])
    threadONE.start()
    threadTWO.start()
#Implementação das funções RECEBER e ENVIAR Mensagem
def receiveMsg(client):
    #Sempre esperando recebr mensagem por parte do servidor
    while True:
        try:
            msg = client.recv(2048).decode('utf-8') #reverter de bytes para strings
            print(msg + '\n')
        except:
            print('Não foi possível permanecer conectado ao servidor \n')
            print('Pressione <ENTER> para CONTINUAR')
            #Após o usuário pressionar enter como as duas funções estão rodando
            #paralelamente quem irá rodar após o enter será o input da função SendMesage
            client.close()
            break
def sendMsg(client, username):
    # A sendMsg sempre estará verificando se há alguma Mensagem por parte do cliente.
    while True:
        try:
            msg = input('\n Digite sua mensagem: \n')
            client.send(f'\n <{username}>: {msg} \n'.encode('utf-8')) #transformar string para bytes com o objetivo de ser interpretado pelo sockets
        except:
            return #sair da função
#execução do main
main()