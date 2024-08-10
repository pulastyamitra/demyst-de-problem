# Data Engineering Solution

## Problem 1

### Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Fixed-Width Parser

This process involves reading the specifications that dictate the structure of the fixed-width file, such as column widths and encodings. The Python application then meticulously processes the input file, extracting the data according to these predefined rules and converting it into the more universally recognized and easily manipulable CSV format.

## Requirements

- Python 3.9+
- Docker (optional, for containerized execution)
- Docker Desktop with WSL2 (for Windows users)

## Setup

### Docker Setup (For Spark Anonymizer)

1. **Install Docker**:
   - Follow the instructions on the [Docker website](https://www.docker.com/products/docker-desktop) to install Docker Desktop.

2. **Ensure WSL2 is Installed and Configured** (for Windows users):
   - Install WSL2 following [Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install).
   - Set WSL2 as the default backend for Docker in Docker Desktop settings.

3. **Ensure Docker Desktop is Running**:
   - Start Docker Desktop and ensure it is running properly.


### Python file indexing folder structure

```bash
├── 01FileParser
│   ├── src
│   │   ├── main.py
│   ├── util
│   │   ├── file_parser.py
│   │   ├── file_spec.py
│   │   ├── generate.py
│   ├── test
│   │   ├── spec.json
│   │   ├── test_file_parser.py
│   │   ├── test_generate_sample_file.py