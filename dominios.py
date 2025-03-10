import csv
import socket

# Function to get reverse DNS (PTR record)
def get_domain(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        return domain
    except socket.herror:
        return "No Domain Found"

# Read the CSV file and add domain names
input_file = "output.csv"  # Archivo con las IPs ya analizadas
output_file = "output_with_domains.csv"

with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["Domain"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        ip_address = row["Address"]
        print(f"Resolviendo dominio de {ip_address}...")
        row["Domain"] = get_domain(ip_address)
        writer.writerow(row)

print(f"Proceso terminado. Revisa el archivo {output_file}")
