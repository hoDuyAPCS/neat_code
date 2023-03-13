#DOWNLOAD JPG IMAGES FROM A WEBSITE - USING BEAUTIFULSOUP 
import requests
from bs4 import BeautifulSoup
import re #regular expression

url = 'https://tienphong.vn/gia-xang-dau-du-bao-tang-nhe-vao-chieu-nay-post1517041.tpo'
response = requests.get(url) # Send an HTTP request to the URL and get the response
soup = BeautifulSoup(response.content, "html.parser") # Use BeautifulSoup to parse the HTML content of the webpage
img_tags = soup.find_all("img") # Find all image tags on the webpage

regex1 = '(\w+)(\.\w+)+(?!.*(\w+)(\.\w+)+)' #get all file name in url
regex2 = '(\w+)(\.(JPG|jpg))' #get only JPG file name

for img in img_tags:
    img_url = img.get("src")
    print('url:',img_url)
    try:
      find_image_to_download = re.search(regex2, img_url)
    except:
      find_image_to_download = False
    
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
      
#CONNECT TO LOCAL HOST SQL DATABASE 
import pyodbc as odbc

conn_str = 'Driver={SQL Server};Server=172.18.5.133,49172;Database=FindMe;Uid=user;Pwd=password;'
#port : 49172
#wifi host : 172.18.5.133

test_conn = odbc.connect(conn_str)
print (test_conn)

cursor = test_conn.cursor()
cursor.execute('SELECT * FROM Album')
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
test_conn.close()
