import time
import socket

#Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1)

try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping {} {}'.format(i, time.ctime(start))
        try:
            # send the message to the server
            sent = sock.sendto(message.encode(), server_addr)
            print("Sent " + message)

            # receive the response from the server
            data, server = sock.recvfrom(4096)
            print("Received " + data.decode())

            # Calculate the round trip time
            end = time.time()
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")

        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")

# Close the socket
finally:
    print("closing socket")
    sock.close()