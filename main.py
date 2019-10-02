import urllib.request, json, numpy as np

with urllib.request.urlopen("https://opendata.arcgis.com/datasets/f65b806a61914332b0cba763d8270c66_92.geojson") as url:
    data = json.loads(url.read().decode())
    # print(data)

for key in data.keys():
    print(key)

print("---")
# print(json.dumps(data["type"], indent=4))
# print(len(data["features"]))
# print(data["features"][0]["properties"]["OBJECTID"])        # gets TAZ number?


# print(data["features"][0]["geometry"]["coordinates"][0][1])
# for some reason the list of coordinates is in another list
# it's a list of a list of coordinates (but the outer list only has that 1 list of coords)
# data["features"][0]["geometry"]["coordinates"][0][i] gets index i of list of coords

avg_TAZ = {}

for TAZ_obj in data["features"]:
    TAZ_num = TAZ_obj["properties"]["OBJECTID"]     # gets TAZ number
    # print(TAZ_num)
    avg_coord = np.average(TAZ_obj["geometry"]["coordinates"][0], axis=0)
    # for coord in TAZ_obj["geometry"]["coordinates"][0]:
    #     print(coord)
    #     break

    avg_TAZ[TAZ_num] = avg_coord
first_five = {k: avg_TAZ[k] for k in list(avg_TAZ)[:5]}

print(first_five)

for key, value in first_five.items():
    print(key, value)

# print(json.dumps(data["features"][0]"geometry"]["coordinates"], indent=4))
# print(json.dumps(data["features"], indent=4))
# print(data["features"][0])
# print(json.dumps(data["type"], indent=4))

# start_avg = np.array([[1, 2, 2], [1, 2, 1], [1, 1, 1]])
# end_avg = np.average(start_avg, axis=0)
# print(end_avg)



print("hello")
