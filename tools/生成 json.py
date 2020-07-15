import csv
import json
import os


def msp(li, filename="../airports.json"):
    v = {}
    for a in li:
        v[a['IATA']] = {
            "IATA": a['IATA'],
            "ICAO": a['ICAO'],
            "city": a['city'] if a['city'] else a['city_en'],
            "city_en": a['city_en'],
            "country": a['country'],
            "name": a['name'] if a['name'] else a['name_en'],
            "name_en": a['name_en'],
            "position": [
                float(a['latitude']),
                float(a['longitude'])
            ],
            "timezone":  a['timezone']
        }
        if 'province' in a:
            v[a['IATA']]['province'] = a['province']
        if 'region' in a:
            v[a['IATA']]['region'] = a['region']

    with open(filename, "w", encoding="utf-8") as w:
        json.dump(
            v, w,
            # separators=(',', ':'),
            indent=4,
            sort_keys=True,
            # ensure_ascii=False
        )


if __name__ == "__main__":
    u = []
    for i in os.listdir("../raw_data/Airports"):
        with open(os.path.join("../raw_data/Airports", i), encoding="utf-8") as w:
            print(i)
            a = list(csv.DictReader(w))
            u += a
            if i.split(".")[0] != "Others":
                msp(a, "../airports_{}.json".format(i.split(".")[0]))

    msp(u)
