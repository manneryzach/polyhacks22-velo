import requests
import pandas as pd

token = 'pk.eyJ1IjoiY2FybGt0IiwiYSI6ImNremswbGFxbzExbG8ybnBhMGc4aTRxNjAifQ.eO1vcS0sYVskxH8FWG_mnQ'

def query_location(query, lat, lon):
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json?proximity={lon}%2C{lat}&types=place%2Cpostcode%2Caddress&access_token={token}').json()
    df = pd.DataFrame(response['features'])
    return df.loc[:,['place_name', 'center']]
    # , df['geometry']

# print(query_location("Montreal"))