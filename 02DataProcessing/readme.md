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

## Data Anonymization

Dask and Apache Spark are both excellent choices for distributed processing. Dask is known for its ability to handle complex, irregular data workflows and integrates well with existing Python ecosystems. On the other hand, Apache Spark is renowned for its speed and support for a wide range of programming languages. I have used Dask to process the file in parallel. The auto scale is configured based on client machine, which can optimize resource usage and cost efficiency. Both tools have their unique strengths and can be selected based on specific project requirements and infrastructure.

## Requirements

- Python 3.9+
- Docker (optional, for containerized execution)
- Docker Desktop with WSL2 (for Windows users)
- Dask (for distributed computing)

## Setup

### Docker Setup (For Spark Anonymizer)

1. **Install Docker**:
   - Follow the instructions on the [Docker website](https://www.docker.com/products/docker-desktop) to install Docker Desktop.

2. **Ensure WSL2 is Installed and Configured** (for Windows users):
   - Install WSL2 following [Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install).
   - Set WSL2 as the default backend for Docker in Docker Desktop settings.

3. **Ensure Docker Desktop is Running**:
   - Start Docker Desktop and ensure it is running properly.

4. **pip install the requirements.txt**:
   - Run the following command to install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
5. **Dask**:
   - The [Dask website](https://docs.dask.org/en/stable/) for reference.


### Python file indexing folder structure

```bash
├── 02DataProcessing
│   ├── src
│   │   ├── main.py
│   ├── util
│   │   ├── data_anonymiser.py
│   │   ├── generate_sample_data.py
│   ├── test
│   │   ├── test_data_anonymiser.py
