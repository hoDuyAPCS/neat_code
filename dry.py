#DOWNLOAD JPG IMAGES FROM A WEBSITE - USING BEAUTIFULSOUP 
import requests
from bs4 import BeautifulSoup

url = 'https://vm.vnexpress.net/thu-vien-anh?match_id=28&q=90897&g-recaptcha-response=03AFY_a8XUBjMOwvb2sPh8o533WjkxWG3AazDa3kUV4ggWgodDjmAxjniZscMJYXQ1Pm8k7_T4T_L_mYnlXRer-pgKn4-5V527lpMnGqiBxhJguUL1yyznjf2bST29sPMQU20HTzQ4gwoNUXx-3G1BQzmiOllxoT4CwzHp-PMqcVefeeu6GGovRHxIEpbq6_SnAFM2Ea3m5llvNiArvXfST1UVPA8IOeZ-TOSM3am2Hun-bdLsCwnrqIj02ig7cBzs3t_FkU-1K9tvPXJRTeAAdTYlbghsviElR6Qy3_2P3UEjzwAJtB0csz0IL1x2ziG5eYmr-R6Rw4XN0cdlS4lGN6-YthH08UtocgrD69qA8H_6nhuWnOYPBPdtl82N9qQomCBHZkK1l4i4-IQhcoV8lt0P5LLdZXLSqwVMaM-GZ1azSK31YDP2YdZR_4l5yMjWRyRpwFWkRoL2S3FRfONOr-37_8-Bkv3zo3yR10h2OI1ENiUW3cHqmcP_5w4YRLYa_gPhK6f_zka3hRzm0J5QjL26kX4y3gXnqg'
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
      

