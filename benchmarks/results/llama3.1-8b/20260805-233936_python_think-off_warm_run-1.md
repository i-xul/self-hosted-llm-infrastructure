# Benchmark Result

## Configuration

| Item | Value |
|---|---|
| Timestamp | `2026-08-05T23:40:56.520191+03:00` |
| Batch timestamp | `20260805-233936` |
| Run | `1/1` |
| Model | `llama3.1:8b` |
| Prompt | `python.md` |
| Run type | `warm` |
| Thinking | `off` |
| Context size | `4096` |
| Temperature | `0` |
| Seed | `42` |

## Environment

| Item | Value |
|---|---|
| Operating system | `Windows-11-10.0.26200-SP0` |
| Machine architecture | `AMD64` |
| Python version | `3.13.14` |
| Python implementation | `CPython` |
| Ollama version | `0.32.5` |
| Model format | `gguf` |
| Model family | `llama` |
| Model families | `llama` |
| Parameter size | `8.0B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Metrics

| Metric | Value |
|---|---:|
| Total duration | 7.559 s |
| Model load duration | 0.158 s |
| Prompt tokens | 86 |
| Prompt evaluation duration | 0.08 s |
| Generated tokens | 570 |
| Generation duration | 7.291 s |
| Generation speed | 78.18 tokens/s |

## Prompt

```text
Write a complete Python 3 program that checks whether a TCP port is open.

Requirements:

- Accept the hostname and port as command-line arguments.
- Use only the Python standard library.
- Use a configurable connection timeout.
- Handle invalid hostnames and connection errors.
- Return an appropriate exit code.
- Include clear error messages.
- Briefly explain how to run the program.
```

## Response

**tcp_port_checker.py**
```python
import sys
import socket

def check_tcp_port(hostname, port):
    """
    Check if a TCP port is open.

    Args:
        hostname (str): Hostname or IP address to connect to.
        port (int): Port number to check.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set connection timeout (default 1 second)
        sock.settimeout(1.0)

        # Try to connect to the host and port
        result = sock.connect_ex((hostname, port))

        # If the connection was successful, the port is open
        return result == 0

    except socket.gaierror:
        # Handle invalid hostname or IP address
        print(f"Error: Invalid hostname '{hostname}'")
        sys.exit(1)

    except ConnectionRefusedError:
        # Handle connection refused error (port closed)
        print(f"Error: Port {port} is closed on host '{hostname}'")
        sys.exit(2)

    except socket.timeout:
        # Handle connection timeout
        print(f"Error: Connection to port {port} on host '{hostname}' timed out")
        sys.exit(3)

    except Exception as e:
        # Catch any other exceptions and exit with an error code
        print(f"Error: Unexpected exception occurred - {e}")
        sys.exit(4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tcp_port_checker.py <hostname> <port>")
        sys.exit(5)

    hostname = sys.argv[1]
    port = int(sys.argv[2])

    result = check_tcp_port(hostname, port)
    if result:
        print(f"Port {port} is open on host '{hostname}'")
        sys.exit(0)
    else:
        print(f"Port {port} is closed on host '{hostname}'")
        sys.exit(1)
```
**How to run the program:**

Save this code in a file named `tcp_port_checker.py`. Then, you can run it from the command line like this:

```bash
python tcp_port_checker.py example.com 80
```

Replace `example.com` with the hostname or IP address of the host you want to check, and `80` with the port number you want to check. The program will print a message indicating whether the port is open or closed, and exit with an appropriate status code.

Note: This program uses the `socket` module from the Python standard library, which provides a simple way to create network sockets and perform basic networking operations.

