from LxmlSoup import LxmlSoup
import requests
import os
if not os.path.exists('audio'):
    os.makedirs('audio')

search_url = 'https://fridaynightfunking.fandom.com/wiki/Vs._Dave_and_Bambi/Music'

html = requests.get(search_url).text

soup =LxmlSoup(html)
audiolist =soup.find_all('audio', class_="mw-file-element")

for audio in audiolist:
    audioSrc =audio.get("src")
    print(audioSrc)

    try:
        if audioSrc.startswith("http"):
            response = requests.get(audioSrc,stream=True)
            response.raise_for_status()
            filename =os.path.join("audio", audioSrc.split("/")[7])

            with open(filename,"wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
    except Exception as error:
        print("не удалось скачать музик    ",error)


    