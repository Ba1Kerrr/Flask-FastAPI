import threading
import time

import requests

images = ["https://rare-gallery.com/uploads/posts/795837-Cats-Eyes-Glance-Whiskers-Snout-Nose.jpg",
          "https://wallbox.ru/wallpapers/main/201546/13dcd7162ea7a31.jpg",
          "https://i.pinimg.com/originals/5b/e2/56/5be25606a1b0a0e951600ec09c4147f1.jpg",
          "https://i.artfile.ru/2137x1412_600336_[www.ArtFile.ru].jpg"]

start_time = time.time()


def download(url: str):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f'Файл {url} скачан за {time.time() - start_time:.2f}')


threads = []

for url in images:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
