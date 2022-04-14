from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import requests
import json
import psycopg2


TOTAL_ITEMS = 374
URL = 'https://ru.tbc.wowhead.com/items/weapons/daggers'
TYPE = 'weapon'
QUERY = """INSERT INTO backend_weapon (name, quality, socket, html_tooltip, icon, stats, subtype, reqclass, uniq) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
item_urls = []
items = []

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)

    page_count = TOTAL_ITEMS // 50 + 1

    for page in range(page_count):
        print()
        print('-------- Page ' + str(page + 1) + ' --------')
        print()
        full_url = URL + f'#items;{page * 50}' if page else URL

        browser.get(full_url)
        browser.refresh()

        items = browser.find_elements(By.CSS_SELECTOR, 'tr.listview-row')
        print(f'Items were found: {len(items)}\n')
        for item in items:
            item_urls.append(item.find_element(By.TAG_NAME, 'a').get_attribute('href').split('/')[3].split('=')[1])
finally:
    print(len(item_urls))
    browser.quit()

if item_urls:
    try:
        connection = psycopg2.connect(user='postgres',
                                        password='admin',
                                        host='localhost',
                                        port='5433',
                                        database="smite_db")
        cursor = connection.cursor()

        items = []
        for url in item_urls:
            print()
            print(f'adding {url}')
            item = []
            p = requests.get(f'https://ru.tbc.wowhead.com/item={url}&xml')
            xml = etree.fromstring(p.text[38:])

            item.append(xml[0].find('name').text)
            item.append(xml[0].find('quality').attrib['id'])
            inventory_slot = xml[0].find('inventorySlot')
            item.append(int(inventory_slot.attrib['id']))
            item.append(xml[0].find('htmlTooltip').text)
            item.append(xml[0].find('icon').text)

            json_equip = json.loads('{' + xml[0].find('jsonEquip').text + '}')

            if 'classes' in json_equip:
                reqclass = json_equip['classes']
                del json_equip['classes']
            else:
                reqclass = None

            if 'maxcount' in json_equip:
                uniq = True
                del json_equip['maxcount']
            else:
                uniq = False

            if 'appearances' in json_equip: del json_equip['appearances']
            if 'displayid' in json_equip: del json_equip['displayid']
            if 'sellprice' in json_equip: del json_equip['sellprice']
            if 'slotbak' in json_equip: del json_equip['slotbak']
            if 'reqlevel' in json_equip: del json_equip['reqlevel']
            if 'dura' in json_equip: del json_equip['dura']
            if 'sheathtype' in json_equip: del json_equip['sheathtype']

            item.append(json.dumps(json_equip))
            subclass = xml[0].find('subclass')
            item.append(int(subclass.attrib['id']))
            item.append(reqclass)
            item.append(uniq)

            items.append(item)

        cursor.executemany(QUERY, items)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into table")
    except (Exception, psycopg2.Error) as error:
        print(error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")