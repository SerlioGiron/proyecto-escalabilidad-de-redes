import csv
from ipwhois import IPWhois

# Function to perform WHOIS lookup
def whois_lookup(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        return res.get('network', {}).get('name', 'N/A')
    except Exception as e:
        return str(e)

# Read the CSV and perform lookups
with open('pruebawireshark.csv', mode='r') as infile, open('output.csv', mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['AS Organization']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        row['AS Organization'] = whois_lookup(row['Address'])
        writer.writerow(row)
