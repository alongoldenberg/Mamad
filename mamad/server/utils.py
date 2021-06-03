import geopy.distance
import pandas as pd
import requests
import googlemaps

GOOGLE_MAPS_API_KEY = "AIzaSyDTBSlx_wqWNJ9UPu52t9dYD3DtmoaZ1FA"
SAFE_ROOMS_FILE_LOCATION = "../resources/tlv_shelters.csv"

def create_google_maps_client():
    return googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def load_shelters():
    return pd.read_csv(SAFE_ROOMS_FILE_LOCATION)

def nearest_shelter(location: tuple, shelters: pd.DataFrame):
    shelters["distance"] = pd.apply(lambda row: get_distance(location, (row["x"], row["y"])))
    return shelters.min(level="distance")

def get_distance(x, y):
    return geopy.distance.vincenty(x, y).km

def get_walking_distance(gm_client: googlemaps.client, source, dest):
    resp = gm_client.distance_matrix(source, dest, mode="walking")
    walking_dist = resp["rows"][0]["elements"][0]["distance"]["value"]
    return walking_dist

def get_walking_time(gm_client: googlemaps.client, source, dest):
    resp = gm_client.distance_matrix(source, dest, mode="walking")
    walking_time = resp["rows"][0]["elements"][0]["duration"]["value"]
    return walki    ng_time
