from socket import *

# server_address=('',9977)# assign the port
serverport = 9977
serverSocket = socket(AF_INET, SOCK_STREAM)  # create a tcp server(craete the socket)
serverSocket.bind(('', serverport))  # connected the server to the port
serverSocket.listen(1)  # listen=  to see every request and accept it
while True:
    print("the [Server] is ready to receive ......")
    connectionSocket, client_address = serverSocket.accept()  # accept, opens a new socket
    data = connectionSocket.recv(1048).decode()  # reads the data from the client
    # print("IP:"+client_address[0]+"port" + str(client_address))
    print(data)
    IP = client_address[0]
    port = client_address[1]
    browser_lines = data.split('\n')
    browser = browser_lines[0]
    client_req_url = ""
    if len(browser_lines) > 1:
        client_req_url = browser.split()[1]
        try:
            if client_req_url == '/' or client_req_url == '/index.html' or client_req_url == '/main_en.html' or client_req_url == '/en':
                connectionSocket.send('HTTP/1.1 200 OK \r\n'.encode())
                connectionSocket.send("Content-Type:text/html\r\n".encode())
                connectionSocket.send("\r\n".encode())
                html_english = open("main_en.html", encoding="utf-8").read()
                connectionSocket.send(html_english.encode())
            elif client_req_url =='/ar' or client_req_url.endswith('main_ar.html'):
                connectionSocket.send('HTTP/1.1 200 OK \r\n'.encode())
                connectionSocket.send("Content-Type:text/html\r\n".encode())
                connectionSocket.send("\r\n".encode())
                html_arabic = open("main_ar.html", encoding="utf-8").read()
                connectionSocket.send(html_arabic.encode())
            elif client_req_url =='/.html':
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type:text/html\r\n".encode())
                connectionSocket.send("\r\n".encode())
                any_html = open("main_any.html", "rb").read()  # open english html file
                connectionSocket.send(any_html)
            elif client_req_url =='/style.css' or client_req_url.endswith('.css'):
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type:text/css\r\n".encode())
                connectionSocket.send("\r\n".encode())
                style_css = open("style.css", "rb").read()  # open english html file
                connectionSocket.send(style_css)

            elif client_req_url.endswith(".png"):
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type:image/png\r\n".encode())
                connectionSocket.send("\r\n".encode())
                png_image = open("images/black.png", "rb").read()  # open english html file
                connectionSocket.send(png_image)
            elif client_req_url.endswith(".jpg"):
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type:image/jpeg\r\n".encode())
                connectionSocket.send("\r\n".encode())
                jpg_image = open("images/nasa-Q1p7bh3SHj8-unsplash.jpg", "rb").read()  # open english html file
                connectionSocket.send(jpg_image)
            elif client_req_url == '/yt':
                redirect_link=b'HTTP/1.1 307 Temporary Redirect\nLOCATION:https://www.youtube.com/\n\n '
                connectionSocket.sendall(redirect_link)
            elif client_req_url == '/so':
                redirect_link=b'HTTP/1.1 307 Temporary Redirect\nLOCATION:https://stackoverflow.com/\n\n '
                connectionSocket.sendall(redirect_link)
            elif client_req_url == '/rt':
                redirect_link=b'HTTP/1.1 307 Temporary Redirect\nLOCATION:https://ritaj.birzeit.edu/register/\n\n '
                connectionSocket.sendall(redirect_link)
            else:
                # Send a 404 Not Found response
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
                connectionSocket.send('Content-Type: text/html\r\n'.encode())
                connectionSocket.send('\r\n'.encode())
                connectionSocket.send('\r\n'.encode())
                f = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8"/>
                    <title>Error-404</title>
                </head>
                <style>
                    body {{
                        background: #bcefff;
                        background-image: -webkit-gradient(radial, 50% 50%, 0, 50% 50%, 800);
                        padding-top: 5%;
                        padding-left: 40%;
                    }}

                    img {{
                        width: 250px;
                        height: 250px;
                    }}

                    .names {{
                        margin-top: 50px;
                        margin-bottom: 50px;
                        font: bold;
                    }}
                </style>
                <body>
                <div class="error_page">
                    <h1 style="color: red">The file is not found</h1>
                    <div class="names">
                        <p><b>Malak Nassar - 1200757</b></p>
                        <p><b>Tala Jebrini - 1200493</b></p>
                        <p><b>Aya Dahbour - 1201738</b></p>
                        <p><b>Hadeel Froukh - 1201585</b></p>
                        <p><b>IP: {ip} Port: {port}</b></p>
                    </div>
                </div>
                </body>
                </html>
                """

                response = f.format(ip=IP, port=port)
                connectionSocket.send(response.encode())

        finally:
            connectionSocket.close()
