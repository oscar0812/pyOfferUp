from lib import places, fetch

if __name__ == '__main__':
    print(places.available_states())
    print(places.available_cities("Texas"))
    posts = fetch.get_posts(query="table", state="Texas", city="Mcallen", limit=100)
    a = 1