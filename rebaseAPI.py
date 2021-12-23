import requests
import zipfile
import io
import sys

def csv2sqlite(input, output):
    url = 'https://www.rebasedata.com/api/v1/convert?outputFormat=sqlite'
    files = {'files[]': open('country_info.csv', 'r')}
    r = requests.post(url, files=files)

    with zipfile.ZipFile(io.BytesIO(r.content)) as zip_ref:
        zip_ref.extractall(output)

if __name__ == '__main__':
    args = sys.argv
    if args[1]:
        input = args[1]
        output = args[2] if len(args)==3 else './'
        csv2sqlite(input, output)