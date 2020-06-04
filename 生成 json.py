import csv
import json
import os


def msp(li, filename="airports.json"):
    v = {}
    for a in li:
        v[a['IATA']] = {
            "IATA": a['IATA'],
            "ICAO": a['ICAO'],
            "city": a['city'],
            "city_en": a['city_en'],
            "country": a['country'],
            "name": a['name'],
            "name_en": a['name_en'],
            "position": [
                float(a['latitude']),
                float(a['longitude'])
            ],
            "timezone":  a['timezone']
        }

    with open(filename, "w", encoding="utf-8") as w:
        json.dump(v, w, sort_keys=True, indent=2, ensure_ascii=False)
    return v


if __name__ == "__main__":
    u = []
    for i in os.listdir("raw_data/Airports"):
        with open(os.path.join("raw_data/Airports", i), encoding="utf-8") as w:
            a = list(csv.DictReader(w))
            u += a
            if i.split(".")[0] != "Others":
                msp(a, "airports_{}.json".format(i.split(".")[0]))

    msp(u)
