import socket
import time
HOST = '192.168.1.30'  # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print ('Exit para sair\n')

while True:
	try:
		## lendo mensagem
		msg = input("Digite algo => ")

		# enviando
		tempoAntes = time.time()
		socket_udp.sendto(str.encode(msg), dest)

		if msg == "EXIT":
			print ("Fim de chat")
			break
		pass

		# lendo resposta
		socket_udp.settimeout(0.256)
		resposta = socket_udp.recv(1024)
		tempoDepois = time.time()
		print ('Resposta => ', resposta.decode())
		print ('tempo = >', tempoDepois - tempoAntes)
	except:
		print ("timeout")
pass

socket_udp.close()