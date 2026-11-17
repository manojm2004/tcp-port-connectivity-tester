import socket

PORTS = [22, 53, 80, 443, 3389, 8080]

def test_host(host):
    print(f'Testing service connectivity to {host}...')
    for p in PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        res = sock.connect_ex((host, p))
        status = 'OPEN' if res == 0 else 'CLOSED / FILTERED'
        print(f'  Port {p:5d} -> {status}')
        sock.close()

if __name__ == '__main__':
    test_host('127.0.0.1')
