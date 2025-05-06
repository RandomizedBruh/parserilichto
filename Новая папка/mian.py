from LxmlSoup import LxmlSoup
import requests
import os
if not os.path.exists('music'):
    os.makedirs('music')

original_url ='ssilachka kakaya nibud'

html = requests.get(original_url).text

soup =LxmlSoup(html)

links =soup.find_all('button', class_ ="small-button")


for link in links:
    url = link.get("onclick").split("'")[1]
    # print(link.get('onclick').split("'")[1])
    if not url.startswith('http'):
        url =f'https://www.myinstants.com{url}'

    try:
        response=requests.get(url,stream=True)
        response.raise_for_status()
        filename=os.path.join('music',url.split('/')[-1])
        with open(filename,'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f'file save: {filename}')

    except Exception as e:
        print(f'Error pri save {url}: {e}')