import pickle
import json
import numpy as np
import pandas as pd
__locations = None
__data_columns = None
__model = None


def get_prediction(strain, RD, conf_pressure, location):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    a = np.zeros(len(__data_columns))

    a[0] = strain
    a[1] = RD
    a[2] = conf_pressure
    if loc_index >= 0:
        a[loc_index] = 1

    data_array = np.array([a])
    df = pd.DataFrame(data=data_array, columns= __data_columns )
    return __model.predict(df)[0]




def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns_2.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are strain,	RD	,conf_pressure

    global __model
    if __model is None:
        with open('./artifacts/gbygmax.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())

    print(get_prediction(10,30.0,100,'Yc'))