__author__ = 'Bamba'


import csv
import scipy.io
import json
import os

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
    return metafields, values


def load_from_mat_file(filename):
    data = {}

    mat = scipy.io.loadmat(path + filename)
    keys = list(mat['data'].dtype.fields)

    for el in keys:
        data[el] = []
        for itm in mat['data'][el][0][0]:
            data[el].append(itm)

    return data


def load_every_mat_in_dir():
    for filename in os.listdir(path):
        if filename.split(".")[1] == "mat":
            yield filename.split(".")[0], load_from_mat_file(filename)



def fetch_meta_data(metafields, row):
    md = {}
    for f in metafields:
        if f == "":
            md["num"] = row[metafields.index(f)]
        else:
            md[f] = row[metafields.index(f)]
    return md
