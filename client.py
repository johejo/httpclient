import requests
import sys


def main():
    num = int(sys.argv[1])
    url = sys.argv[2]

    length = int(get_length(url))
    text = get_text(url, num, length)
    print(text)


def get_length(url):
    r = requests.head(url)
    return r.headers['Content-Length']


def get_text(url, num, length):
    text = ''
    byte = 0
    chunk_size = int(length / num)
    reminder = int(length % num)

    if reminder != 0:
        num += 1

    for i in range(num):
        if i == num:
            chunk_size = reminder

        headers = {'Range': 'bytes={0}-{1}'.format(byte, byte + chunk_size - 1)}

        byte += chunk_size

        r = requests.get(url, headers=headers)
        if r.status_code == 206:

            text += r.text

        elif r.status_code == 200:
            text = r.text
            break

        else:
            text = r.status_code
            break

    return text


if __name__ == '__main__':
    main()
