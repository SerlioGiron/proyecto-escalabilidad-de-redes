import csv
import requests
import time

# API Endpoint
API_URL = "https://ipinfo.io/{}/json"

# Function to get IP information using ipinfo.io API
def get_ip_info(ip):
    try:
        response = requests.get(API_URL.format(ip), timeout=3)  # Timeout de 3 segundos
        data = response.json()
        return data.get("org", "N/A")  # Devuelve la organización (AS Organization)
    except requests.exceptions.RequestException:
        return "Timeout/Error"

# Leer el archivo CSV original
input_file = "pruebawireshark.csv"  # Cambia esto por el nombre de tu archivo CSV original
output_file = "outputapi.csv"  # Archivo CSV con los resultados

with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["AS Organization"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for row in reader:
        ip_address = row["Address"]
        print(f"Consultando {ip_address}...")  # Muestra progreso en la terminal
        row["AS Organization"] = get_ip_info(ip_address)
        writer.writerow(row)
        time.sleep(1)  # Pequeña pausa para evitar bloqueos de la API

print(f"Proceso terminado. Revisa el archivo {output_file}")
