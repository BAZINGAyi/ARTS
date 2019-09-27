

class Server(object):

    @staticmethod
    def tcp_server():
        from socketserver import BaseRequestHandler, TCPServer

        class EchoHandler(BaseRequestHandler):
            def handle(self):
                print('Got connection from', self.client_address)
                while True:
                    msg = self.request.recv(8192)
                    print('---receive client message:----', msg)
                    if not msg:
                        break
                    self.request.send(msg)

        serv = TCPServer(('', 20000), EchoHandler)
        serv.serve_forever()

    @staticmethod
    def tcp_client():
        from socket import socket, AF_INET, SOCK_STREAM
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 20000))
        s.send(b'Hello')
        msg = s.recv(8192)
        print('---receive server message:----', msg)

    @staticmethod
    def stream_request_handler():
        from socketserver import StreamRequestHandler, TCPServer

        class EchoHandler(StreamRequestHandler):
            def handle(self):
                print('Got connection from', self.client_address)
                # self.rfile is a file-like object for reading
                for line in self.rfile:
                    # self.wfile is a file-like object for writing
                    self.wfile.write(line)

        serv = TCPServer(('', 20000), EchoHandler)
        serv.serve_forever()


    @staticmethod
    def server_support_more_clients():
        """
        使用 ForkingTCPServer 或者 ThreadingTCPServer 会为每个客户端
        创建一个新的进程或者线程。
        :return:
        """
        from socketserver import ThreadingTCPServer
        from socketserver import BaseRequestHandler

        class EchoHandler(BaseRequestHandler):
            def handle(self):
                print('Got connection from', self.client_address)
                while True:
                    msg = self.request.recv(8192)
                    print('---receive client message:----', msg)
                    if not msg:
                        break
                    self.request.send(msg)
        serv = ThreadingTCPServer(('', 20000), EchoHandler)
        serv.serve_forever()


    @staticmethod
    def fixed_up_server_support_more_clients():
        """
        但由于客户端连接数没有限制，因此可以同时发送大量的
        连接让你的服务器崩溃。

        预防这个问题，可以预先分配固定的线程池或进程池。创建一个普通非线程服务器，然后在一个
        线程中使用 serve_forever() 来启动
        :return:
        """
        from threading import Thread
        from socketserver import TCPServer
        from socketserver import BaseRequestHandler

        class EchoHandler(BaseRequestHandler):
            def handle(self):
                print('Got connection from', self.client_address)
                while True:
                    msg = self.request.recv(8192)
                    print('---receive client message:----', msg)
                    if not msg:
                        break
                    self.request.send(msg)

        NWORKERS = 16
        serv = TCPServer(('', 20000), EchoHandler)
        for n in range(NWORKERS):
            t = Thread(target=serv.serve_forever)
            t.daemon = True
            t.start()
        serv.serve_forever()


    @staticmethod
    def change_socket_configuration():
        """
        设置参数 bind_and_activate=False 来修改 socket 参数
        设置参数 TCPServer.allow_reuse_address = True， 来允许服务器重新绑定一个
        之前使用过的端口号
         TCPServer.allow_reuse_address = True
         serv = TCPServer(('', 20000), EchoHandler)
         serv.serve_forever()
        :return:
        """
        from socketserver import TCPServer
        from socketserver import BaseRequestHandler
        from socket import socket

        class EchoHandler(BaseRequestHandler):
            def handle(self):
                print('Got connection from', self.client_address)
                while True:
                    msg = self.request.recv(8192)
                    print('---receive client message:----', msg)
                    if not msg:
                        break
                    self.request.send(msg)

        serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
        # Set up various socket options
        serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # Bind and activate
        serv.server_bind()
        serv.server_activate()
        serv.serve_forever()

    @staticmethod
    def change_server_configuration():
        import socket
        from socketserver import StreamRequestHandler, TCPServer

        class EchoHandler(StreamRequestHandler):
            # Optional settings (defaults shown)
            timeout = 5  # Timeout on all socket operations
            rbufsize = -1  # Read buffer size
            wbufsize = 0  # Write buffer size
            disable_nagle_algorithm = False  # Sets TCP_NODELAY socket option

            def handle(self):
                print('Got connection from', self.client_address)
                try:
                    for line in self.rfile:
                        # self.wfile is a file-like object for writing
                        self.wfile.write(line)
                except socket.timeout:
                    print('Timed out!')

    @staticmethod
    def build_a_server_with_native_sockets():
        from socket import socket, AF_INET, SOCK_STREAM

        def echo_handler(address, client_sock):
            print('Got connection from {}'.format(address))
            while True:
                msg = client_sock.recv(8192)
                if not msg:
                    break
                client_sock.sendall(msg)
            client_sock.close()

        def echo_server(address, backlog=5):
            sock = socket(AF_INET, SOCK_STREAM)
            sock.bind(address)
            sock.listen(backlog)
            while True:
                client_sock, client_addr = sock.accept()
                echo_handler(client_addr, client_sock)

        echo_server(('', 20000))


if __name__ == '__main__':
    # 实现一个 TCP 服务器和客户端通信, 服务器是单线程的，只能为一个客户端提供服务
    from threading import Thread
    t = Thread(target=Server.tcp_server)
    c = Thread(target=Server.tcp_client)
    c.start()
    t.start()
    t.join()
    c.join()

    # 实现一个流处理服务器, 也只能为一个客户端提供服务
    # Server.stream_request_handler()

    # 实现与多个客户端通信
    # Server.server_support_more_clients()

    # 固定和客户端通信的数量
    # Server.fixed_up_server_support_more_clients()

    # 调整绑定的 socket 配置
    # Server.change_socket_configuration()

    # 使用原始 socket 构建一个 server
    Server.build_a_server_with_native_sockets()