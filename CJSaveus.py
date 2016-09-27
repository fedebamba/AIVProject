__author__ = 'Bamba'


import os
import os.path
import csv
import scipy.io
import json


path = ""
csv_filename = ""

with open("config.json") as config:
    dt = json.load(config)
    path = dt["mat_path"]
    csv_filename = dt["csv_filename"]


def load_from_csv_file():
    values = []
    with open(csv_filename, "r+") as file:
        reader = csv.reader(file)
        metafields = reader.__next__()

        for row in reader:
            values.append(fetch_meta_data(metafields, row))
    return values


def load_from_mat_file(filename):
    data = {}

    mat = scipy.io.loadmat(path + filename)
    keys = list(mat['data'].dtype.fields)

    data["keys"] = keys
    for el in keys:
        data[el] = []
        for itm in mat['data'][el][0][0]:
            data[el].append(itm)

    return data


def fetch_meta_data(metafields, row):
    md = {}
    for f in metafields:
        if f == "":
            md["num"] = row[metafields.index(f)]
        else:
            md[f] = row[metafields.index(f)]
    return md

print(load_from_csv_file())