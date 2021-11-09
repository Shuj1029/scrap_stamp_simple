import requests
from bs4 import BeautifulSoup
import json
from PIL import Image
import sys
import glob

def imageUrl(link, imagename):
    # get HTML
    res = requests.get(link)
    # get beautifulsoup object
    soup = BeautifulSoup(res.text, 'html.parser')
    # extract lists of stamp
    found = soup.find_all('li', class_='mdCMN09Li FnStickerPreviewItem')
    # extract urls or image
    url_list = [json.loads(found[i]['data-preview'])['staticUrl'] for i in range(len(found))]
    # scrap images
    for i, url in enumerate(url_list):
        image = requests.get(url).content
        dst = "output/" + imagename + "/" + imagename + "-" + '{0:02d}'.format(i) + ".png"
        with open(dst, "wb") as f:
            print("download to: " + dst)
            f.write(image)

def imagebigger(imagename, fx, fy):    
    filepaths = "output/" + imagename + "/*.png"
    for filename in glob.glob(filepaths):
        img = Image.open(filename)
        size = (round(img.width * fx), round(img.height * fy))
        im_resized = img.resize(size=(128,128))
        im_resized.save(filename)

if __name__ == "__main__":
    pass
