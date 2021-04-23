## SETUP
link your selenium driver executable_path in fetch.py

## Usage
OfferUp uses latitude and longitude coordinates when fetching data from the API. places.py has 
the coordinates of all the states and cities OfferUp supports (case sensitive). When looking in
a city you must also provide the state the city resides in.

### Available States and cities
```python
from pyOfferUp import places
print(places.available_states())
print(places.available_cities("Texas"))
print(places.available_cities("Alabama"))
```
returns:
```
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
['Abilene', 'Addison', 'Amarillo', 'Arlington', 'Austin', 'Baytown', 'Beaumont', 'Brownsville', 'Bryan', 'Carrollton', 'Cedar Hill', 'Channelview', 'Conroe', 'Corpus Christi', 'Dallas', 'Denton', 'Duncanville', 'El Paso', 'Euless', 'Farmers Branch', 'Fort Worth', 'Frisco', 'Garland', 'Grand Prairie', 'Harlingen', 'Houston', 'Humble', 'Irving', 'Katy', 'Killeen', 'Laredo', 'Lewisville', 'Longview', 'Lubbock', 'Lufkin', 'Mansfield', 'Mcallen', 'McKinney', 'Mesquite', 'Midland', 'Midlothian', 'Nacogdoches', 'Odessa', 'Pearland', 'Pflugerville', 'Plano', 'Port Arthur', 'Richardson', 'Round Rock', 'San Angelo', 'San Antonio', 'San Marcos', 'Sherman', 'Stafford', 'Sugar Land', 'Sweetwater', 'Temple', 'Tomball', 'Tyler', 'Victoria', 'Waco', 'Weslaco', 'Wichita Falls']
['Anniston', 'Birmingham', 'Decatur', 'Dothan', 'Huntsville', 'Mobile', 'Montgomery', 'Selma', 'Tuscaloosa']
```

#### Lookup Example
Look for "luigis mansion" in Mcallen, Texas:
```python
from pyOfferUp import fetch
posts = fetch.get_posts(query="luigis mansion", state="Texas", city="Mcallen", limit=100)
```
returns:
```
[{'type': 'item', 'tile_id': 'c6a1a1b4-3def-4791-b572-f22d55045db1', 'item': {'post_date': '2021-04-23T21:17:04.129Z', 'owner': {'get_profile': {}, 'id': 37122132, 'active': False, 'softBlocked': False}, 'id': 1109700533, 'listing_id': '3cded582-57e5-3e6e-a3a6-528823a6bc6e', 'category': {'id': 17, 'name': 'Business Equipment'}, 'category_v2': {'l1': '12', 'l2': '12.10'}, 'location_name': 'Mercedes, TX', 'title': 'Big Tables , Wood and solid metal!! Pick Up Mercedes Tx', 'get_full_url': 'https://offerup.com/item/detail/1109700533/', 'priority': 100, 'state': 3, 'longitude': -97.905, 'latitude': 26.162, 'sort_label': 'Popular', 'description': '$340, Ashley furniture tables ', 'paid': False, 'payable': True, 'listing_type': 2, 'condition': 40, 'photos': [{'uuid': 'b2744b404ff547d0a5b793c0265c9cd8', 'images': {'detail_full': {'url': 'https://images.offerup.com/A33RTR8HhBUluSLNPmepUcsNQ5k=/1920x996/9073/907317e07aad4203baa8d150c52a3167.jpg', 'width': 1920, 'height': 996}, 'detail': {'url': 'https://images.offerup.com/JgsRWm-ScWbJQWzUPVQGlcS99t0=/481x250/9073/907317e07aad4203baa8d150c52a3167.jpg', 'width': 481, 'height': 250}, 'list': {'url': 'https://images.offerup.com/JgsRWm-ScWbJQWzUPVQGlcS99t0=/481x250/9073/907317e07aad4203baa8d150c52a3167.jpg', 'width': 481, 'height': 250}}}, {'uuid': 'b018c4a0213240b581933deeb6de411a', 'images': {'detail_full': {'url': 'https://images.offerup.com/AYu5HliKVnGA2rUVGXzjoejAkFA=/1922x1442/b018/b018c4a0213240b581933deeb6de411a.jpg', 'width': 1922, 'height': 1442}, 'detail': {'url': 'https://images.offerup.com/yQjecZyW6vi_IxuV1v9_AXxY0qE=/333x250/b018/b018c4a0213240b581933deeb6de411a.jpg', 'width': 333, 'height': 250}, 'list': {'url': 'https://images.offerup.com/yQjecZyW6vi_IxuV1v9_AXxY0qE=/333x250/b018/b018c4a0213240b581933deeb6de411a.jpg', 'width': 333, 'height': 250}}}, {'uuid': '4bf32734d3eb4b90839a5cb9d834079e', 'images': {'detail_full': {'url': 'https://images.offerup.com/AbNNdPuiXqN7xFLJoD0jyvVQa9A=/1922x1442/4bf3/4bf32734d3eb4b90839a5cb9d834079e.jpg', 'width': 1922, 'height': 1442}, 'detail': {'url': 'https://images.offerup.com/P_txzgx6G-2c7juUsbwMNzNWFt8=/333x250/4bf3/4bf32734d3eb4b90839a5cb9d834079e.jpg', 'width': 333, 'height': 250}, 'list': {'url': 'https://images.offerup.com/P_txzgx6G-2c7juUsbwMNzNWFt8=/333x250/4bf3/4bf32734d3eb4b90839a5cb9d834079e.jpg', 'width': 333, 'height': 250}}}, {'uuid': 'e7f775a053114f81b7a22893c3acff1b', 'images': {'detail_full': {'url': 'https://images.offerup.com/tDXFOY8V61rSKhgDtp58bAQLwfU=/1922x1442/e7f7/e7f775a053114f81b7a22893c3acff1b.jpg', 'width': 1922, 'height': 1442}, 'detail': {'url': 'https://images.offerup.com/31Fl3UGWAYzCN8LQoKTrEAbibpM=/333x250/e7f7/e7f775a053114f81b7a22893c3acff1b.jpg', 'width': 333, 'height': 250}, 'list': {'url': 'https://images.offerup.com/31Fl3UGWAYzCN8LQoKTrEAbibpM=/333x250/e7f7/e7f775a053114f81b7a22893c3acff1b.jpg', 'width': 333, 'height': 250}}}], 'price': '340', 'shipping_attributes': {'shipping_enabled': False, 'show_as_shipped': False, 'can_ship_to_buyer': False, 'buy_it_now_enabled': False, 'seller_pays_shipping': False, 'feed_show_shipping_icon': False, 'seller_manages_shipping': False, 'empty': False}, 'local_pickup_enabled': True, 'zipcode': '78570', 'quantity': 1, 'is_merchant_item': False, 'visible': True}}, {...}]
```

