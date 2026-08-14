# Benchmark Result

## Configuration

| Item | Value |
|---|---|
| Timestamp | `2026-08-14T11:15:42.855443+03:00` |
| Batch timestamp | `20260814-111325` |
| Run | `1/1` |
| Model | `phi4:14b` |
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
| Python version | `3.13.15` |
| Python implementation | `CPython` |
| Ollama version | `0.32.9` |
| Model format | `gguf` |
| Model family | `phi3` |
| Model families | `phi3` |
| Parameter size | `14.7B` |
| Quantization | `Q4_K_M` |
| Model context length | `16384` |

## Metrics

| Metric | Value |
|---|---:|
| Total duration | 16.928 s |
| Model load duration | 0.086 s |
| Prompt tokens | 86 |
| Prompt evaluation duration | 0.116 s |
| Generated tokens | 764 |
| Generation duration | 16.688 s |
| Generation speed | 45.78 tokens/s |

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

Below is a complete Python 3 program that checks whether a TCP port is open, meeting all your specified requirements:

```python
import socket
import sys
import argparse

def check_port(host, port, timeout):
    try:
        # Create a new socket using IPv4 and TCP protocols
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Set the connection timeout
            sock.settimeout(timeout)
            
            # Attempt to connect to the specified host and port
            result = sock.connect_ex((host, port))
            
            # If result is 0, the port is open
            if result == 0:
                print(f"Port {port} on {host} is open.")
                return True
            else:
                print(f"Port {port} on {host} is closed or unreachable.")
                return False

    except socket.gaierror:
        # Handle invalid hostnames
        print(f"Error: Invalid hostname '{host}'.")
        sys.exit(1)
    except socket.timeout:
        # Handle connection timeout
        print(f"Error: Connection to {host}:{port} timed out after {timeout} seconds.")
        sys.exit(2)
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        sys.exit(3)

def main():
    parser = argparse.ArgumentParser(description="Check if a TCP port is open on a given host.")
    
    # Add command-line arguments for hostname, port, and timeout
    parser.add_argument("host", type=str, help="Hostname or IP address to check")
    parser.add_argument("port", type=int, help="Port number to check")
    parser.add_argument("--timeout", type=float, default=5.0, help="Connection timeout in seconds (default: 5.0)")
    
    args = parser.parse_args()
    
    # Call the function with parsed arguments
    check_port(args.host, args.port, args.timeout)

if __name__ == "__main__":
    main()
```

### Explanation

- **Command-line Arguments**: The program uses `argparse` to handle command-line inputs. It requires a hostname and port number as positional arguments and accepts an optional timeout argument.
  
- **Socket Connection**: It creates a TCP socket using `socket.AF_INET` for IPv4 and `socket.SOCK_STREAM` for TCP.

- **Timeout Handling**: The connection timeout is configurable via the `--timeout` option, defaulting to 5 seconds if not specified.

- **Error Handling**:
  - `socket.gaierror`: Catches invalid hostnames.
  - `socket.timeout`: Handles cases where the connection attempt times out.
  - General exceptions are caught and reported for any other errors.

- **Exit Codes**:
  - `0` indicates success (port is open).
  - `1` for an invalid hostname.
  - `2` for a timeout error.
  - `3` for any other exception.

### How to Run the Program

1. Save the script to a file, e.g., `check_port.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the program using Python:

   ```bash
   python check_port.py <hostname> <port> [--timeout <seconds>]
   ```

   Replace `<hostname>` with the target host, `<port>` with the port number you want to check, and optionally specify a timeout in seconds.

Example usage:

```bash
python check_port.py example.com 80 --timeout 10
```

This command checks if port 80 on `example.com` is open, with a connection timeout of 10 seconds.

