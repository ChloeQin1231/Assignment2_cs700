# Testing Documentation for UDPPingerClient

## Testing Environment

- **Localhost Environment**: Testing was performed on a single machine with both the client and server running on `localhost` (127.0.0.1). This environment was used to verify basic functionality and handling of packet loss simulation within a controlled environment.


## Test Cases

### Successful Ping
- **Description**: The client sends a ping message to the server, which is expected to echo the message back to the client.
- **Expected Outcome**: The client receives the echoed message and calculates the RTT.
- **Actual Outcome**: As expected, the client successfully received responses from the server for the majority of the pings and calculated the RTTs.
### Packet Loss Simulation
- **Description**: The server is programmed to randomly drop packets with a 30% probability to simulate packet loss.
- **Expected Outcome**: The client occasionally times out and prints "Request timed out" for dropped packets.
- **Actual Outcome**: The client behavior matched the expectations, timing out for 3 pings, indicating simulated packet loss.
### Handling of Timeout
- **Description**: The client waits up to 1 second for a response from the server before timing out.
- **Expected Outcome**: If the server does not respond within 1 second, the client prints "Request timed out".
- **Actual Outcome**: The client correctly handled timeouts, printing the timeout message whenever responses were delayed beyond 1 second. 