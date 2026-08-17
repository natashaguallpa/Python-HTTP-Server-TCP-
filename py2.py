from socket import *

#Create a TCP server socket 
#Code Start

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Code End 


while True: 
	#Establish the connection
	print("The server is ready to receive")
	connectionSocket, addr = serverSocket.accept() 
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open("./html_files/" + filename[1:])
		outputdata = f.read()
		
		#Send HTTP OK and the Set-Cookie header into the socket 
		# set the cookie to whatever value you'd like 
		

		connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
		connectionSocket.send("Content-Type: text/html\r\n".encode())
		connectionSocket.send("Set-Cookie: assignment_cookie=sucess; Max-Age=3600\r\n".encode())
		connectionSocket.send("\r\n".encode())

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())

		#close the socket
		connectionSocket.close()

	except IOError:
			#send HTTP NotFound reponse 
			
			response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
			response += "<html><body><h1>404 Not Found</h1></body></html>"
			connectionSocket.send(response.encode())


			connectionSocket.close()
			

serverSocket.close()
