import requests
from bs4 import BeautifulSoup
import fake_useragent
import csv
import re
import json
import datetime
import time

def connect_with_site(link):
    """
    Function of connect to site

    :param link: link of site
    :return: page of site by link
    """
    with open('proxy') as file:
        proxy_base = ''.join(file.readlines()).strip().split('\n')
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user, 'accept': '*/*'}
    req = requests.get(link, headers=header)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup

# list_items_motors_sum = []

def get_links_of_motors(soup):
    list_items_motors = []
    list_items = soup.find('div', class_="tx-dkm-products").find_all("a")
    for item in list_items:
        list_items_motors.append('https://www.dunkermotoren.com' + item.get("href"))
    return list_items_motors
def get_data(list_items_motors):
    for i in range(0, len(list_items_motors)-1):
        motor_url = list_items_motors[i]

        req2 = requests.get(motor_url, headers=header)
        soup2 = BeautifulSoup(req2.text, 'lxml')

        motor_title = soup2.h1.text


        motor_img = link[0:29] + soup2.find("figure").find("a").get("href")
        motor_description = soup2.find(class_="ce-bodytext").find("p").text

        motor_feature_dict = dict()
        motor_feature_tr = soup2.find(class_ = "ce-table").find_all("tr")
        # for tr_ in motor_feature_tr:
        #     motor_feature_td = tr_.find_all("td")
        #     #dict_ = {}
        #     for td_ in motor_feature_td:
        #         td = re.sub("^\s+|\n|\r|\s+$", '', td_.text)
        #         row.append(td)
        #     motor_feature_dict[row[0]] = row[1] + ' ' + row[2]

        list_items_motors_sum.append({
                'motor_url': motor_url,
                'motor_title': motor_title,
                'motor_img': motor_img,
            })
#
#
#     # Сохраняем в формат JSON и открываем файл
# with open("all_motors_dict.json", "w", encoding="utf-8") as file:
#     json.dump(list_items_motors_sum, file, indent=4, ensure_ascii=False)
def main():
    soup = connect_with_site('https://www.dunkermotoren.com/en/products/')
    list_items_motors = get_links_of_motors(soup)
    get_data(list_items_motors)








if __name__== "__main__":
    main()