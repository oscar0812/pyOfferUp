import json
import requests

from pyOfferUp import places
from pyOfferUp.constants import *


def __post_request__(request_body):
    s = requests.Session()
    response = s.get(ENDPOINT)
    cookies = dict(response.cookies)
    response = s.post(ENDPOINT + "/api/graphql",
                      request_body,
                      headers={"Content-Type": "application/json",
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},
                      verify=False,
                      cookies=cookies)

    data: dict = {}

    if response.status_code == 200:
        data = json.loads(response.content)

    return data


# get state and city from places.py
def get_listings(query, state, city=None, limit=50, pickup_distance=50, price_min=None, price_max=None,
                 sort: SORT = SORT.NEWEST_FIRST,
                 delivery: DELIVERY = DELIVERY.PICKUP,
                 conditions=None):
    if conditions is None:
        conditions = []

    lat, lon = places.get_lat_lon(state, city)
    return get_listings_by_lat_lon(query, lat, lon, limit, pickup_distance, price_min, price_max, sort, delivery,
                                   conditions)


# get posts by latitude and longitude
def get_listings_by_lat_lon(query, lat, lon, limit=50, pickup_distance=50, price_min=None, price_max=None,
                            sort: SORT = SORT.NEWEST_FIRST,
                            delivery: DELIVERY = DELIVERY.PICKUP,
                            conditions: list[CONDITION] = None):
    if conditions is None:
        conditions = []

    search_params = [{"key": "q", "value": query},
                     {"key": "distance", "value": str(pickup_distance)},
                     {"key": "platform", "value": "web"},
                     {"key": "lon", "value": str(lon)},
                     {"key": "lat", "value": str(lat)},
                     {"key": "limit", "value": str(limit)},
                     {"key": "SORT", "value": sort.value},
                     {"key": "DELIVERY_FLAGS", "value": delivery.value},
                     {"key": "searchSessionId", "value": ""}]

    if price_min is not None:
        search_params.append({"key": "PRICE_MIN", "value": price_min})

    if price_max is not None:
        search_params.append({"key": "PRICE_MAX", "value": price_max})

    if len(conditions) > 0:
        conditions_str = ",".join([str(c.value) for c in conditions])
        search_params.append({"key": "CONDITION", "value": conditions_str})

    request_body = json.dumps({"operationName": "GetModularFeed", "variables": {"searchParams": search_params},
                               "query": GRAPHQL.MODULAR_FEED.value})

    response = __post_request__(request_body)
    listings = []

    if 'data' in response and 'modularFeed' in response['data'] and 'looseTiles' in response['data']['modularFeed']:
        listings = [lt['listing'] for lt in response['data']['modularFeed']['looseTiles'] if 'listing' in lt]

        for listing in listings:
            listing['listingUrl'] = ENDPOINT + "/item/detail/" + listing['listingId']

    return listings


def get_listing_details(listing_id):
    variables = {"isLoggedIn": False, "listingId": listing_id}
    request_body = json.dumps(
        {"operationName": "GetListingDetailByListingId", "variables": variables, "query": GRAPHQL.LISTING_DETAIL.value})
    return __post_request__(request_body)
