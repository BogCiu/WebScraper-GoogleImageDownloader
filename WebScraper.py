import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

PATH = os.getcwd() + "\chromedriver.exe"

wd = webdriver.Chrome(PATH)

downloaded_image_type ="real animal cat"
amount_downloaded = 5
try:
    downloaded_image_type = sys.argv[1]
except:
    pass
try:
    amount_downloaded = int(sys.argv[2])
except:
    pass

def get_image(image_type, wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url1 = "https://www.google.com/search?q="
    url2 = "&tbm=isch&ved=2ahUKEwi13KrhtIT0AhUBOuwKHR1eCFoQ2-cCegQIABAA&oq="
    url3 = "&gs_lcp=CgNpbWcQAzIECAAQEzIICAAQCBAeEBMyCAgAEAgQHhATMggIABAIEB4QEzIICAAQCBAeEBMyCAgAEAgQHhATMggIABAIEB4QEzoECAAQQzoICAAQgAQQsQM6BQgAEIAEOgsIABCABBCxAxCDAToECAAQHjoICAAQBRAeEBNQpAVY4h1g3x5oB3AAeACAAXyIAcQNkgEEMTYuM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=h8-GYfX8M4H0sAedvKHQBQ&bih=969&biw=1920#imgrc=JIF3l2FXswiASM"
    image_type = image_type.replace(" ", "+")
    url = url1 + image_type + url2 + image_type + url3
    wd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        end = wd.find_elements(By.CLASS_NAME, "OuJzKb Yu2Dnd")

        for img in thumbnails[len(image_urls) + skips: max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            for image in images:
                if image.get_attribute("src") in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute("src") and "http" in image.get_attribute("src"):
                    image_urls.add(image.get_attribute("src"))
                    # print("Added")

            if end:
                # print("Reached the end")
                break

    return image_urls


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, 'JPEG')

        # print("Done")
    except Exception as e:
        print("Failed on", e)


urls = get_image(downloaded_image_type, wd, 1, amount_downloaded)

os.mkdir(downloaded_image_type)

for i, url in enumerate(urls):
    download_image(downloaded_image_type + "/", url, downloaded_image_type + " " + str(i) + ".jpg")

wd.quit()
