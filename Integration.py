import json
import pandas as pd

names = [
    "bts",
    "itzy",
    "kpop",
    "seventeen",
    "twice",
]

json_data = {}

for name in names:
    filename = "data_" + name + ".json"
    with open(filename, "r") as f:
        json_data["data_" + name] = json.load(f)
        
df = pd.read_csv("tracks_group.csv")

json_data["tracks_total"] = df.shape[0]

count = 0
for name in names:
    count_this = df[df["grouping"] == name].shape[0]
    json_data["tracks_" + name] = count_this
    count += count_this
    
json_data["tracks_kpop"] = count + df[df["grouping"] == "kpop"].shape[0]
    
with open("data.json", "w") as f:
    json.dump(json_data, f)