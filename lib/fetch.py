import enum
import json
import urllib

from selenium import webdriver
from lib import places

options = webdriver.ChromeOptions()
user_agent = 'MMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'C:\Users\oscar\PycharmProjects\pyOfferUp\chromedriver.exe',
                          chrome_options=options)


class SORT_BY(enum.Enum):
    NEWEST_FIRST = "-posted"
    CLOSEST_FIRST = "distance"
    PRICE_LOW_TO_HIGH = "price"
    PRICE_HIGH_TO_LOW = "-price"


class PURCHASE_BY(enum.Enum):
    PICKUP = "p"
    SHIPPING = "s"
    PICKUP_AND_SHIPPING = "p_s"


def get_posts(query, state, city=None, limit=50, pickup_distance=50, price_min=0, price_max=1000000,
              sort: SORT_BY = SORT_BY.NEWEST_FIRST,
              purchase_by: PURCHASE_BY = PURCHASE_BY.PICKUP):
    lat, lon = places.get_lat_lon(state, city)
    api_url = "https://offerup.com/webapi/search/v4/feed/?lat={lat}&lon={lon}&limit={limit}" \
              "&platform=web&experiment_id=experimentmodel24&q={query}&sort={sort}&radius={radius}" \
              "&price_min={price_min}&price_max={price_max}&delivery_param={dp}" \
        .format(lat=lat, lon=lon, limit=limit, query=urllib.parse.quote(query), sort=sort.value, radius=pickup_distance,
                price_min=price_min, price_max=price_max, dp=purchase_by)

    driver.get(api_url)
    pre = driver.find_element_by_tag_name("pre").text
    return json.loads(pre)['data']['feed_items']
