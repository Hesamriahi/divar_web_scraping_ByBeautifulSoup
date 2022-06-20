# import time
from index_module.models import Advertise
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
import requests
from bs4 import BeautifulSoup

# import threading


# import asyncio

# from schedule import every, repeat, run_pending
# import time
#
#
# @repeat(every(10).seconds)
def import_from_divar():
    # threading.Timer(20.0, import_from_divar).start()

    url = 'https://divar.ir/s/gorgan'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    advertises = soup.findAll('section', {'class': 'post-card-item kt-col-6 kt-col-xxl-4'})

    saveList = []
    for advertise in advertises:
        try:
            advertiseDict = {
                'title': advertise.find('div', {'class': 'kt-post-card__title'}),
                'price': advertise.find('div', {'class': 'kt-post-card__description'}),
                'description': advertise.find('span', {'class': 'kt-post-card__bottom-description kt-text-truncate'}),
                'url_link': 'https://divar.ir' + (advertise.select_one('a')['href']).strip(),
            }
            saveList.append(advertiseDict)

        except:
            pass

    saveList.reverse()

    for ad in saveList:
        try:
            hereSlug = PurePosixPath(unquote(urlparse(ad['url_link']).path)).parts[-1]
            check_unique_inDB: bool = Advertise.objects.filter(slug__iexact=hereSlug).exists()
            if check_unique_inDB == False:
                new_advertise = Advertise(title=ad['title'].text,
                                          price=ad['price'].text if ad['price'] is not None else '',
                                          description=ad['description'].text if ad['description'] is not None else '',
                                          advertise_url=ad['url_link'],
                                          slug=hereSlug)

        except:
            pass

    print('driver.close()')
