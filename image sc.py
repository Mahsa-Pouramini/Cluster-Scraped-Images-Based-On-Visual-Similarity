
from bs4 import BeautifulSoup
import urllib.request
import requests

number = 0
for page_num in range(1, 278):

    url = "https://www.digikala.com/search/category-women-shoes/?pageno={}".format(page_num)

    response = requests.get(url)
    # if response.status_code != 200:
    #     print(f"Status: {response.status_code} — Try rerunning the code\n")
    # else:
    #     print(f"Status: {response.status_code}\n")
    soup = BeautifulSoup(response.content, "html.parser")
    content = soup.find("div", {'class':'o-page__content'})
    images = content.find_all('img')
    final_images = []

    for i in images:
        if 'svg' not in str(i['src']):
            final_images.append(i['src'])
    temp1 = number
    for image in final_images:
        urllib.request.urlretrieve(image, str(number) + '.jpg')
        number += 1
    temp2 = number
    print('successfully saved ', temp2 - temp1, 'images on this page.')
    print('page {} completed.'.format(page_num))