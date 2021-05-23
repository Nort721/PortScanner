import threading
import socket
import sys
from datetime import datetime

open_ports = []


def scan_ports(name, start_port, max_port):
    try:
        for port in range(start_port, max_port):
            if (port - 1) == max_port - 1:
                print(name, "is finishing its tasks")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))  # returns an error indicator
            if result == 0:
                open_ports.append(port)
            s.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Could not connect to server")
        sys.exit()


if __name__ == '__main__':
    print("-" * 50)
    print("Port scanner by Nort721")
    print("-" * 50)

    target_ip = input('Enter target ip: ')
    start_port = int(input('starting port: '))
    max_ports = int(input('ending port: '))
    threads_count = int(input('threads count: '))

    threads = []

    i = 0
    next_max = start_port
    min_port = start_port
    while i < threads_count:
        i += 1
        next_max += ((max_ports - start_port) // threads_count)
        if i == threads_count:
            next_max = max_ports
        print("Thread{} starts: {} ends: {}".format(i, min_port, next_max))
        threads.append(threading.Thread(target=scan_ports, args=("thread{}".format(i), min_port, next_max)))
        min_port = next_max

    print("-" * 50)
    print("Scanning for open ports in range {}-{} . . .".format(start_port, max_ports))
    print("Time started: " + str(datetime.now()))
    print("-" * 50)

    for var in threads:
        var.start()

    for var in threads:
        var.join()

    print("Done scanning")
    print("Time Ended: " + str(datetime.now()))

    if len(open_ports) == 0:
        print("no open ports found in range {}-{}".format(start_port, max_ports))
    else:
        print("open ports found:")
        print("-" * 50)
        for port in open_ports:
            print(port)
        print("-" * 50)

    input("press close to exit . . .")
