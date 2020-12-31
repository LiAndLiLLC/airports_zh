import csv
import json
import os


def msp(source, target, index_key, prettify=True):
    with open(source, encoding="utf-8") as w1:
        rv = {
            a[index_key]: {
                key: a[key] for key in a
            } for a in list(csv.DictReader(w1))
        }
    with open(target, "w", encoding="utf-8") as w2:
        if prettify:
            json.dump(rv, w2, indent=2, sort_keys=True, ensure_ascii=False)
        else:
            json.dump(rv, w2, separators=(',', ':'))


if __name__ == "__main__":
    msp(source="../raw_data/Airlines/airlines.csv",
        target="../airlines.json", index_key="IATA", prettify=False)
    msp(source="../raw_data/Regions/regions.csv",
        target="../regions.json", index_key="code", prettify=False)
