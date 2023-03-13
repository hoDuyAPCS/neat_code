#DOWNLOAD JPG IMAGES FROM A WEBSITE - USING BEAUTIFULSOUP 
import requests
from bs4 import BeautifulSoup

url = 'https://vnexpress.net/nhung-co-gai-nghien-chay-bo-4578025.html'
response = requests.get(url) # Send an HTTP request to the URL and get the response
soup = BeautifulSoup(response.content, "html.parser") # Use BeautifulSoup to parse the HTML content of the webpage
img_tags = soup.find_all("img") # Find all image tags on the webpage

regex1 = '(\w+)(\.\w+)+(?!.*(\w+)(\.\w+)+)' #get all file name in url
regex2 = '(\w+)(\.JPG)' #get only JPG file name

for img in img_tags:
    img_url = img.get("src")
    print(img_url)
    find_image_to_download = re.search(regex2, img_url)
    
    if find_image_to_download:
      download_image = requests.get(img_url)
      image_name = find_image_to_download.group(1)
      with open(image_name+".JPG", "wb") as f: 
        f.write(download_image.content) #save image to local machine
      print('downloaded and saved:',image_name+".JPG")
    else:
      print('skip')
    
#SHOW IMAGE IN LOCAL
from PIL import Image

image = Image.open('image_name.JPG')
image.show()
      

