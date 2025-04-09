import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def download_images(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for img in image_tags:
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = os.path.join(folder_path, img_name)
            
            try:
                img_data = requests.get(img_url).content
                with open(img_path, 'wb') as f:
                    f.write(img_data)
                print(f"Downloaded {img_name}")
            except Exception as e:
                print(f"Error downloading {img_name}: {str(e)}")

# Example usage:
url_to_scrape = 'https://elzerowebschool.github.io/Bootstrap_5_Design_01_Bondi/'
folder_to_save = './Assets'

download_images(url_to_scrape, folder_to_save)
