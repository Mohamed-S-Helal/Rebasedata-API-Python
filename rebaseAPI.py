import requests
import zipfile
import io

def csv2sqlite(csv, output):
    url = 'https://www.rebasedata.com/api/v1/convert?outputFormat=sqlite'
    files = {'files[]': open('country_info.csv', 'r')}
    r = requests.post(url, files=files)

    with zipfile.ZipFile(io.BytesIO(r.content)) as zip_ref:
        zip_ref.extractall('./')

if __name__ == '__main__':
    csv2sqlite('country_info.csv', './')