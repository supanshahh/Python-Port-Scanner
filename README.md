# Python Port Scanner

A simple multithreaded port scanner built in Python while learning networking and cybersecurity fundamentals.

## Features

* Scan a target host for open TCP ports
* Supports custom port ranges
* Uses Python sockets for network connections
* Uses multithreading for faster scanning
* Resolves hostnames to IP addresses

## How It Works

The scanner creates TCP socket connections to a target host and attempts to connect to each port in the specified range.

If a connection is successful, the port is reported as open.

## Usage

```bash
py Python_Port_Scanner.py google.com 1 100
```

### Parameters

* TARGET - Hostname or IP address
* START_PORT - Starting port number
* END_PORT - Ending port number

## Example

```bash
py Python_Port_Scanner.py scanme.nmap.org 20 100
```

Example Output:

```text
Scanning Target 45.33.32.156
Port 22 is open
Port 80 is open
```

## Technologies Used

* Python
* Socket Programming
* Multithreading
* Git
* GitHub

## What I Learned

While building this project I learned:

* Command-line arguments (`sys.argv`)
* Socket programming
* TCP connections
* Port scanning fundamentals
* Python threading
* Git and GitHub workflow

## Future Improvements

* Service detection (HTTP, HTTPS, SSH, etc.)
* Save results to a file
* Better error handling
* Banner grabbing
* GUI version
