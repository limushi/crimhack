import json
import os,sys,logging
from tqdm import tqdm

def append_district_by_street(filename="2016-10-20_gms_stat.json", streetfield = "gmr_address"):
    with open("moscow_buildings.json") as bigfile:
        streetData = json.load(bigfile)
        
    with open(filename, "r") as datafile:
        data = json.load(datafile)
    
    for new_item in tqdm(data):
        
        for item in streetData['rows']:
            if new_item[streetfield] and item['street_name'] and "district" not in new_item.keys():
                if item['street_name'].split(" ")[0].strip().replace("ё","е") in new_item[streetfield].replace("ё","е"):
                    new_item['district'] = item['area_name']
                    break
        if "district" not in new_item.keys():
            print("Not found addr %s" % str(new_item[streetfield]))
                    
    print("Done %s addrs" % str(len([item for item in data if "district" in item.keys()])))                
                    
    with open("districts_"+filename, 'w') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)     
        
def make_by_district(district):
    with open("moscow_buildings.json") as bigfile:
        data = json.load(bigfile)
        data2 = []
        for item in data['rows']:
            if district in item['area_name']:
                
                new_item = {}
                new_item['address'] = item['address']
                new_item['district'] = item['area_name']
                
                data2.append(new_item)
        
        with open(district.replace(" ", "_") + "_" + "streets.json", "w") as streetfile:
            json.dump(data2, streetfile)            
        
def main():
    with open("moscow_buildings.json") as bigfile:
        data = json.load(bigfile)
        data2 = []
        for item in data['rows']:
            new_item = {}
            new_item['address'] = item['address']
            new_item['district'] = item['area_name']
            data2.append(new_item)
            
        with open("streets_districts.json", "w") as streetfile:
            json.dump(data2, streetfile)    