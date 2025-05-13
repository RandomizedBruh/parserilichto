from LxmlSoup import LxmlSoup
import requests
import os
if not os.path.exists('imags'):
    os.makedirs('imags')

search_url = 'https://fridaynightfunking.fandom.com/wiki/Vs._Dave_and_Bambi/Gallery'

html = requests.get(search_url).text

soup =LxmlSoup(html)
imglist =soup.find_all('img', class_ ="thumbimage")
for img in imglist: 
    imgSrc= img.get("src")
    print(imgSrc)

    try:
        if imgSrc.startswith("http"):
            response = requests.get(imgSrc,stream=True)
            response.raise_for_status()
            filename =os.path.join("imags", imgSrc.split("/")[7])

            with open(filename,"wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
    except Exception as error:
        print("не удалось скачать имг    ",error)
        
