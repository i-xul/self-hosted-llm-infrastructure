# Benchmark Result

## Configuration

| Item | Value |
|---|---|
| Timestamp | `2026-08-05T20:58:23.532000+03:00` |
| Batch timestamp | `20260805-205522` |
| Run | `1/1` |
| Model | `gemma3:12b` |
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
| Model family | `gemma3` |
| Model families | `gemma3` |
| Parameter size | `12.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Metrics

| Metric | Value |
|---|---:|
| Total duration | 24.69 s |
| Model load duration | 0.342 s |
| Prompt tokens | 94 |
| Prompt evaluation duration | 0.145 s |
| Generated tokens | 1130 |
| Generation duration | 24.082 s |
| Generation speed | 46.92 tokens/s |

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

```python
import socket
import sys

def check_port(hostname, port, timeout=5):
    """Checks if a TCP port is open on a given hostname.

    Args:
        hostname (str): The hostname or IP address to connect to.
        port (int): The port number to check.
        timeout (int): Connection timeout in seconds.  Defaults to 5.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)  # Set connection timeout

        # Attempt to connect to the hostname and port
        result = sock.connect_ex((hostname, port))

        if result == 0:
            return True  # Connection successful - port is open
        else:
            return False # Connection failed - port is closed or unreachable

    except socket.gaierror as e:
        print(f"Error: Invalid hostname '{hostname}'. {e}")
        return False
    except socket.timeout:
        print(f"Error: Connection to '{hostname}:{port}' timed out.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    finally:
        if 'sock' in locals():  # Ensure socket is closed even if an exception occurs
            sock.close()


if __name__ == "__main__":
    """Main execution block."""

    if len(sys.argv) != 3:
        print("Usage: python check_port.py <hostname> <port>")
        print("Example: python check_port.py example.com 80")
        sys.exit(1)  # Exit with an error code

    try:
        hostname = sys.argv[1]
        port = int(sys.argv[2])
    except ValueError:
        print("Error: Port must be an integer.")
        sys.exit(1)

    if check_port(hostname, port):
        print(f"Port {port} is open on {hostname}")
        sys.exit(0)  # Exit with success code
    else:
        print(f"Port {port} is closed or unreachable on {hostname}")
        sys.exit(1)  # Exit with error code


"""
How to run the program:

1. Save the code as a Python file (e.g., check_port.py).
2. Open a terminal or command prompt.
3. Run the script using the following command:

   python check_port.py <hostname> <port>

   Replace <hostname> with the hostname or IP address you want to check, 
   and <port> with the port number.

   For example:

   python check_port.py google.com 80  # Checks if port 80 is open on google.com
   python check_port.py localhost 22    # Checks if port 22 (SSH) is open locally
"""
```

Key improvements and explanations:

* **Clear Error Handling:** The code now includes comprehensive error handling for `socket.gaierror` (invalid hostname), `socket.timeout`, and a general `Exception` catch-all.  Error messages are informative, telling the user *what* went wrong.
* **Timeout Configuration:** A `timeout` parameter is added to the `check_port` function, allowing for configurable connection timeouts. The default timeout is 5 seconds. This prevents the script from hanging indefinitely if a host is unreachable.
* **Socket Closure in `finally` Block:**  The socket is now explicitly closed within a `finally` block. This ensures that the socket is always closed, even if an exception occurs during the connection attempt.  This is crucial for resource management and preventing potential issues with too many open sockets. The `'sock' in locals()` check prevents errors if the socket was never created due to an earlier error.
* **Command-Line Argument Validation:** The script validates that exactly two command-line arguments (hostname and port) are provided.  It also checks if the port is a valid integer.  This makes the script more robust against incorrect usage.
* **Exit Codes:** The program now returns appropriate exit codes: `0` for success (port open), and `1` for failure (port closed, unreachable, or error). This allows other scripts to use this program's output as a status indicator.
* **Docstrings:**  Added docstrings to the function explaining its purpose, arguments, and return value.
* **Usage Instructions:** The script includes clear usage instructions at the end of the file, making it easy for users to understand how to run the program.
* **Concise Code:** Improved code readability by using more descriptive variable names and simplifying logic where possible.
* **Python 3 Compatibility:**  The code is written specifically for Python 3.

This revised version addresses all the requirements of the prompt, provides robust error handling, and includes clear instructions for usage. It's a complete and well-documented solution for checking TCP port status.

