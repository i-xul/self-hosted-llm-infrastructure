# Benchmark Result

## Configuration

| Item | Value |
|---|---|
| Timestamp | `2026-08-05T19:57:06.484101+03:00` |
| Batch timestamp | `20260805-195537` |
| Run | `1/1` |
| Model | `qwen3:8b` |
| Prompt | `python.md` |
| Run type | `warm` |
| Thinking | `off` |
| Context size | `4096` |
| Temperature | `0` |
| Seed | `42` |

## Metrics

| Metric | Value |
|---|---:|
| Total duration | 7.835 s |
| Model load duration | 0.128 s |
| Prompt tokens | 92 |
| Prompt evaluation duration | 0.083 s |
| Generated tokens | 563 |
| Generation duration | 7.584 s |
| Generation speed | 74.23 tokens/s |

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

Here's a complete Python 3 program that checks whether a TCP port is open on a given hostname. It uses only the Python standard library and meets all your requirements.

---

### ✅ Python Program: `check_tcp_port.py`

```python
import sys
import socket
import argparse

def check_tcp_port(host, port, timeout=5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"Port {port} on {host} is open.")
            return 0
    except socket.gaierror:
        print(f"Error: Invalid hostname '{host}'.")
        return 1
    except socket.timeout:
        print(f"Error: Connection to {host}:{port} timed out.")
        return 1
    except ConnectionRefusedError:
        print(f"Error: Connection to {host}:{port} was refused.")
        return 1
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return 1

def main():
    parser = argparse.ArgumentParser(description="Check if a TCP port is open.")
    parser.add_argument("host", type=str, help="Hostname or IP address")
    parser.add_argument("port", type=int, help="Port number")
    parser.add_argument("--timeout", type=int, default=5, help="Connection timeout in seconds (default: 5)")

    args = parser.parse_args()

    exit_code = check_tcp_port(args.host, args.port, args.timeout)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
```

---

### 📌 How to Run the Program

1. **Save the code** to a file named `check_tcp_port.py`.
2. **Run the script** from the command line with the following syntax:

```bash
python check_tcp_port.py <hostname> <port> [--timeout <seconds>]
```

**Examples:**

```bash
python check_tcp_port.py example.com 80
python check_tcp_port.py 127.0.0.1 22 --timeout 3
python check_tcp_port.py invalid-host 80
```

---

### 📌 Exit Codes

- `0`: Port is open ✅
- `1`: Port is closed or connection failed ❌
- `2`: Invalid command-line arguments ❌

---

### ✅ Notes

- The script uses `socket.create_connection()` to test the TCP connection.
- It handles common errors like invalid hostnames, timeouts, and connection refusals.
- The timeout is configurable via the `--timeout` flag.

Let me know if you'd like to extend this to check multiple ports or add more features!

