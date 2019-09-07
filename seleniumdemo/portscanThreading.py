import threading
import time
from queue import Queue
import socket


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!!!!!!!!!!!')
        con.close()

    except:
        with print_lock:
            print('port', port, 'is closed')


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


if __name__ == '__main__':

    print_lock = threading.Lock()
    target = '192.168.1.14'
    q = Queue()

    for x in range(50):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    start = time.time()

    for worker in range(1, 101):
        q.put(worker)

    q.join()
    print('Entire jobs are done', time.time() - start)



