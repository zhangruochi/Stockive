import time
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler


HOST_NAME = 'localhost'
PORT_NUMBER = 8001

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), SimpleHTTPRequestHandler)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))