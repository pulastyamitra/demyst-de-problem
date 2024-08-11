import csv
from faker import Faker

def generate_fake_data(num_records, filename):
    fake = Faker()
    data = []
    columns = ['first_name', 'last_name', 'address', 'date_of_birth']
 
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for _ in range(num_records):
            record = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'date_of_birth': fake.date_of_birth()
            }
            data.append(record)
            writer.writerow(record)
        

# Example usage
if __name__ == "__main__":
    num_records = 1000000
    filename = 'fake_data_l.csv'
    generate_fake_data(num_records, filename)

#C:/Users/04815D744/AppData/Local/Programs/Python/Python311/python.exe "c:/[01] Coding/demyst-de-problem/02DataProcessing/util/generate_sample_data.py"