import machine
import socket
import time


def web_response(ledValue):

    return """
<html>
<head>
    <title>My First Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <script>
    setTimeout(function(){
        window.location.reload(1);
        }, 5000);
    </script>
    <style>
        html{
            font-family: Helvetica;
            display:inline-block;
            margin: 0px auto;
            text-align: center;
            }
        h1{
            color: #0F3376;
            padding: 2vh;
            }test3_webserver
        p{
            font-size: 1.5rem;
            }
        .button{
            display: inline-block;
            background-color: #e7bd3b;
            border: none;
            border-radius: 4px;
            color: white;
            padding: 16px 40px;test3_webserver
            text-decoration: none;
            font-size: 30px;
            margin: 2px;
            cursor: pointer;
            }
        .button2{
            background-color:
            #4286f4;
            }
    </style>
</head>
<body>
    <h1>Hello PyAmsterdam</h1>
    <p>led state: <strong>{""" + ledValue + """}</strong></p>
    <p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p
></body>
</html>"""


def setup_and_run():

    led = machine.PWM(machine.Pin(2))
    ledValue = 'OFF'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:

        conn, addr = s.accept()
        print(addr)
        request = conn.recv(1024)
        request = str(request)
        if '/?led=off' in request:
            led.duty(0)
            ledValue='OFF'
        elif '/?led=on' in request:
            led.duty(1023)
            ledValue='ON'

        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(web_response(ledValue))
        conn.close()

if __name__ == '__main__':
    setup_and_run()
