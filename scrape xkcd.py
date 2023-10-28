import requests
import re
import time
import random
import html


for num in range(1, 2845):

    link = f'https://xkcd.com/{num}/'

    response = requests.get(link)
    coded_content = response.text
    content = html.unescape(coded_content)

    link_image = re.findall(r'<a href= "(.+?)"', content)[0]
    title = re.findall(r'<title>xkcd: (.+?)</', content)[0]
    note = re.findall(r'title="(.+?)"', content)[-1]
    title = re.sub(r'[\/><\?\"\:\|\\\?\*]', '+', title)
    note = re.sub(r'[\/><\?\"\:\|\\\?\*]', '+', note)

    print(response.status_code)
    print(link_image)
    print(title)
    print(note)
    print()

    name_file = f'{num:04} - {title} - {note[:130]}.jpg'

    image_response = requests.get(link_image)
    with open(name_file, 'wb') as f:
        f.write(image_response.content)

    time.sleep(random.random())





