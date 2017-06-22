import requests
import sys

chunk_size = int(sys.argv[1])
url = 'http://www.net.info.hiroshima-cu.ac.jp'

byte = 0
text = ''
initial = 1
size = 0

while True:
    headers = {'Range': 'bytes={0}-{1}'.format(byte, byte + chunk_size - 1)}
    byte += chunk_size
    r = requests.get(url, headers=headers)
    if initial == 1:
        cr = r.headers.get('Content-Range')
        size = int(cr[cr.find('/') + 1:])
        initial = 0

    if byte >= size:
        break

    text += r.text

print(text)
