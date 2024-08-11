import dask.dataframe as dd
import hashlib
from dask.distributed import Client, LocalCluster
import os
import re

def extract_client_machine_info(client_info):
    # Regular expression to find processes and threads
    processes_match = re.search(r'processes=(\d+)', client_info)
    threads_match = re.search(r'threads=(\d+)', client_info)
    memory_limit_match = re.search(r'memory=([\d.]+)\s*GiB', client_info)
    
    # Extract the values
    processes = int(processes_match.group(1)) if processes_match else None
    threads = int(threads_match.group(1)) if threads_match else None
    memory_limit = float(memory_limit_match.group(1)) if memory_limit_match else None
    
    return processes, threads,memory_limit


def hash_column(a_string):
    return hashlib.sha256(a_string.encode('utf-8')).hexdigest()

# Load the data and hash the columns
def anonymise_data(input_file, output_file):
    cluster = LocalCluster()
    client = Client(cluster)
    client_info =  client.__repr__()

    # Extract the client machine information
    processes, threads ,memory = extract_client_machine_info(client_info)

    # get the file size in MB for calculating the number of partitions
    file_size = os.path.getsize(input_file) / (1024 * 1024)

    # calculate the number of partitions for the parquet file based on the file size
    num_partitions = max(1, int(file_size / 128))

    print(f"Dashboard_link : {cluster.dashboard_link}")
    print(f'Processes: {processes}, Threads: {threads}, Memory: {memory} GiB')
    print(f'File Size: {file_size:.2f} MB , Num Partitions: {num_partitions}')

    # Adapt the cluster based on the number of processes
    cluster.adapt(minimum=1, maximum= processes -2) 

    with cluster:
        df = dd.read_csv(input_file)
        df['first_name'] = df['first_name'].apply(hash_column, meta=('first_name', 'object'))
        df['last_name'] = df['last_name'].apply(hash_column, meta=('last_name', 'object'))
        df['address'] = df['address'].apply(hash_column, meta=('address', 'object'))
        df = df.repartition(npartitions=num_partitions)
        df.to_parquet(output_file, engine='pyarrow')
    
    client.close()