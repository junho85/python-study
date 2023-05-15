
def get_hostip1():
    import socket
    return socket.gethostbyname(socket.gethostname())

def get_hostip2():
    import socket
    return socket.gethostbyname(socket.getfqdn())

def get_hostip3():
    import socket
    return socket.gethostbyname(socket.gethostbyaddr(socket.gethostname())[0])

def get_hostip4():
    import socket
    return socket.gethostbyname(socket.gethostbyname_ex(socket.gethostname())[0])

def get_hostip5():
    import socket
    return socket.gethostbyname(socket.gethostbyname_ex(socket.getfqdn())[0])

def get_hostip6():
    import socket
    return socket.gethostbyname(socket.gethostbyname(socket.gethostname()))


print(get_hostip1())
print(get_hostip2())
print(get_hostip3())
print(get_hostip4())
print(get_hostip5())
print(get_hostip6())
