# Basic Port Scanner

**Repository Name:** `basic-port-scanner`

#### README.md

```markdown
# Basic Port Scanner

A simple Python script for scanning open ports on a specified IP address. The script attempts to connect to a range of ports and reports which ones are open.

## Features

- Scans a range of ports on a given IP address.
- Reports open and closed ports.

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/syge852/basic-port-scanner.git
    cd basic-port-scanner
    ```

2. Run the script:

    ```sh
    python port_scanner.py
    ```

3. Enter the target IP address and the range of ports to scan when prompted.

## Example

```sh
Enter the IP address to scan: 192.168.1.1
Enter the starting port: 20
Enter the ending port: 25

Scanning 192.168.1.1 from port 20 to 25...

Port 20: CLOSED
Port 21: OPEN
Port 22: OPEN
Port 23: CLOSED
Port 24: CLOSED
Port 25: CLOSED
