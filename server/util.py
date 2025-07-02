import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    if __model:
        return round(__model.predict([x])[0], 2)
    else:
        return "Model not loaded"

def get_location_names():
    return __locations

def load_saved_artifacts():
    global __locations
    global __data_columns
    global __model

    print("Loading saved artifacts...")

    with open("./artifacts/columns.json") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = [loc.lower() for loc in __data_columns[3:]]  # normaliser en minuscules

    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
