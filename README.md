# Python-HTTP-Server-TCP-
# Python HTTP Server

A simple HTTP web server built from scratch using Python TCP sockets. This project explores how web servers communicate with clients using TCP and the HTTP protocol without relying on a web framework.

## About the Project

The server listens for incoming TCP connections and processes HTTP requests from clients. When a client requests an HTML file, the server retrieves the requested file and sends it back as an HTTP response.

The server also handles missing files by returning a `404 Not Found` response and demonstrates the use of HTTP cookies through the `Set-Cookie` header.

## Features

- Creates a TCP server using Python sockets
- Listens for incoming HTTP requests
- Parses requested filenames from HTTP requests
- Serves HTML files to clients
- Sends `HTTP/1.1 200 OK` responses
- Returns `404 Not Found` for unavailable files
- Sends HTTP `Content-Type` headers
- Sets cookies using the `Set-Cookie` HTTP header
- Handles multiple client requests sequentially

## Technologies Used

- Python
- TCP/IP
- Socket Programming
- HTTP
- HTML
- HTTP Cookies

## How It Works

1. The server creates a TCP socket.
2. The socket binds to port `12345`.
3. The server listens for incoming client connections.
4. An HTTP request is received from the client.
5. The requested filename is extracted from the request.
6. The server searches for the file inside the `html_files` directory.
7. If found, the server returns a `200 OK` response along with the HTML content.
8. If the file cannot be found, the server returns a `404 Not Found` response.
9. The client connection is closed after the response is sent.

## Project Structure

```text
Python-HTTP-Server/
├── py2.py
├── CompNet.html
└── html_files/
```

## Running the Server

Start the server:

```bash
python3 py2.py
```

The server will display:

```text
The server is ready to receive
```

Then access the server through a browser using:

```text
localhost:12345/<filename>
```

## What I Learned

Through this project, I gained hands-on experience with TCP socket programming and learned how HTTP communication works behind the scenes. I also practiced constructing HTTP responses, serving files, handling errors, and working with HTTP headers and cookies.

## Note

This project was created for educational purposes to better understand computer networking, TCP sockets, and the HTTP protocol.
