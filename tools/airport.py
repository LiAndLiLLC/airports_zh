import csv
import sys
from fr24 import fr24_Airport as Airport
from wikipedia import 获取所有语言

if __name__ == "__main__":
    print(sys.argv)
    s = {}
    nodes_to_visit = set(['HKG'])
    visited_nodes = set()
    output = {}
    while len(nodes_to_visit) > 0:
        a = nodes_to_visit.pop()
        if a in visited_nodes:
            continue

        visited_nodes.add(a)

        des = Airport(a).destinations
        p = set()
        for i in des:
            if i['country'] == sys.argv[1].upper() and i['iata'] not in s:
                p.add(i['iata'])
                s[i['iata']] = {
                    "IATA": i['iata'],
                    "ICAO": i['icao'],
                    "city_en": i['city'],
                    "country": sys.argv[2].upper(),
                    "name_en": i['name'],
                    "latitude": float(i['lat']),
                    "longitude": float(i['lon']),
                    "timezone": sys.argv[3]
                }

                rsp = 获取所有语言(i['name'])
                for lang in rsp:
                    s[i['iata']]["name_{}".format(lang)] = rsp[lang]

        nodes_to_visit |= p
        print("{} 有 {} 个邻居 {}".format(a, len(p), len(nodes_to_visit)))

    with open('names2.csv', 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ["country", "ICAO", "IATA", "city_en", "name_en",
                      "latitude", "longitude", "timezone", "city_zh", "name_zh"]
        # for key in s:
        #     fieldnames = fieldnames | set(s[key].keys())
        # fieldnames = sorted(list(fieldnames))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key in s:
            writer.writerow(s[key])
