from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from google_images_download import google_images_download

driver = webdriver.Chrome('/chromedriver')

response = google_images_download.googleimagesdownload()

search_queries = ['dogs', 'cats']
number_of_images = 5

for query in search_queries:
    arguments = {'keywords': query, 'limit': number_of_images, 'print_urls': True}
    paths = response.download(arguments)
    print(paths)

for query in search_queries:
    driver.get('https://www.google.com/search?q=' + query + '&tbm=isch')

    scrolling = 0
    while True:
        driver.execute_script('window.scrollBy(0,10000);')
        time.sleep(5)
        scrolling += 1
        if scrolling == 10:
            break

    elements = driver.find_elements_by_xpath('//a[@class="rg_i"]/img')
    img_urls = [element.get_attribute('src') for element in elements]
    print(img_urls)