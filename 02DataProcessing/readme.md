# Data Engineering Solution

## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

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