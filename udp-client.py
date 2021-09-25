import socket
import time


def chatCliente(socket_udp, dest):
    try:
        entrada = open("entrada.txt", "r")
    except:
        print("Problema ao abrir arquivo")
        return

    info = []

    print("Envindo as mensagens...")

    for linha in entrada:
        # delay de 1 segundo
        time.sleep(1)
        # gravando o tempo no envio da mensagem.
        tempoAntes = time.time()
        # enviando
        socket_udp.sendto(str.encode(linha), dest)

        try:
            # timeout para 256ms
            socket_udp.settimeout(0.256)
            # lendo resposta
            resposta = socket_udp.recv(1024)
            # gravando o tempo na recepção da mensagem
            tempoDepois = time.time()
            # Round Trip Time
            rtt = tempoDepois - tempoAntes

            info.append([resposta, rtt])
        except:
            info.append([linha, "timeout"])

    entrada.close()

    with open("saida.txt", "w") as saida:
        saida.write("\n".join(str(item) for item in info))
        saida.write("\n\n\nRTT=> " + str(rttMedia(info)) + "\n")

    print("Mensagens enviadas com sucesso!")


def rttMedia(info):
    media = 0
    tamanho = 0
    for item in info:
        if(item[1] != "timeout"):
            media += item[1]
            tamanho = tamanho + 1

    return media/tamanho


def main():
    HOST = '192.168.1.30'  # Endereco IP do Servidor
    PORT = 5002            # Porta que o Servidor esta
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    while True:

        msg = input("Deseja fazer uma medição? (S/N) => ")
        if(msg == "S"):
            chatCliente(socket_udp, dest)
        elif(msg == "N"):
            msg = input("Deseja sair do programa? (S/N) => ")
            if(msg == "S"):
                break

    pass

    socket_udp.close()


main()
