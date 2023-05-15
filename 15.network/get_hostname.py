def get_hostname_platform1():
    import platform
    return platform.node()


def get_hostname_platform2():
    import platform
    return platform.uname()[1]


def get_hostname_os1():
    import os
    return os.uname().nodename


def get_hostname_os2():
    import os
    return os.uname()[1]


def get_hostname_subprocess1():
    import subprocess
    return subprocess.check_output('hostname').decode('utf-8').strip()


def get_hostname_socket1():
    import socket
    return socket.gethostname()


def get_hostname_socket2():
    import socket
    return socket.getfqdn()


def get_hostname_socket3():
    import socket
    return socket.gethostbyaddr(socket.gethostname())[0]


def get_hostname_socket4():
    import socket
    return socket.gethostbyname_ex(socket.gethostname())[0]


def get_hostname_socket5():
    import socket
    return socket.gethostbyname_ex(socket.getfqdn())[0]


print("==platform==")
print(get_hostname_platform1())
print(get_hostname_platform2())

print("==os==")
print(get_hostname_os1())
print(get_hostname_os2())

print("==subprocess==")
print(get_hostname_subprocess1())

print("==socket==")
print(get_hostname_socket1())

# 여기서 부터는 왜인지 소문자로 나온다
print(get_hostname_socket2())
print(get_hostname_socket3())
print(get_hostname_socket4())
print(get_hostname_socket5())


# output
"""
==platform==
JunHos-MBP-2.kornet
JunHos-MBP-2.kornet
==os==
JunHos-MBP-2.kornet
JunHos-MBP-2.kornet
==subprocess==
JunHos-MBP-2.kornet
==socket==
JunHos-MBP-2.kornet
junhos-mbp-2.kornet
junhos-mbp-2.kornet
junhos-mbp-2.kornet
junhos-mbp-2.kornet
"""