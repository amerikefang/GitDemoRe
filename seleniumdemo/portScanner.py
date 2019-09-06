import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What website to scan ?: ')


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        return True
    except:
        return False

if __name__ == '__main__':
    for x in range(1, 101):
        if portscan(x):
            print('Port', x, 'is open!!!!')
        else:
            print('Port', x, 'closed')
