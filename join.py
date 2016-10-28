import csv
import os,sys,logging
import json
from tqdm import tqdm


def ege2():
    
    data = []
    
    empty_row = 0
    with open("ege2.csv") as datafile:
        dataCSV = csv.DictReader(datafile)
    
        for row in dataCSV:
            if row['address'] == "":
                empty_row = empty_row + 1
                
            data.append(row)
    
     
    print("Empty addrs left: %s" % str(len([item for item in data if item['address'] == ""])))
    
    print("Empty rows %s" % str(empty_row))
    
    schData = []       
    
    with open('schools.csv') as schoolfile:
        schCSV = csv.DictReader(schoolfile)
        for row in schCSV:
            schData.append(row)
    
    for item in tqdm(data):
        if item['address'] == "":
            for row in schData:
                if item['fullname'] == row['fullname']:
                    item['address'] = row['address']
                    empty_row = empty_row -1
    
    print("Empty row %s" % str(empty_row))

    print('Processed')
    
    print("Empty addrs left: %s" % str(len([item for item in data if item['address'] == ""])))
    
    schData = []
    
    with open('schools_3.csv') as schoolfile:
        schCSV = csv.DictReader(schoolfile)
        for row in schCSV:
            schData.append(row)
    
    for item in tqdm(data):
        if item['address'] == "":
            for row in schData:
                if item['fullname'] == row['FullName']:
                    item['address'] = row['LegalAddress']
                    empty_row = empty_row -1
    
    print("Empty row %s" % str(empty_row))

    print('Processed')
    
    print("Empty addrs left: %s" % str(len([item for item in data if item['address'] == ""])))
    
    schData = []
    
    with open('schools_all.csv') as schoolfile:
        schCSV = csv.DictReader(schoolfile, delimiter=';')
        for row in schCSV:
            schData.append(row)
    
    for item in tqdm(data):
        if item['address'] == "":
            for row in schData:
                if item['fullname'] == row['poln_name']:
                    item['address'] = row['yuridich_adress']
                    empty_row = empty_row -1
    
    print("Empty row %s" % str(empty_row))

    print('Processed')
    
    print("Empty addrs left: %s" % str(len([item for item in data if item['address'] == ""])))

    schData = []       
    
    with open('adress_all.csv') as schoolfile:
        schCSV = csv.DictReader(schoolfile)
        for row in schCSV:
            schData.append(row)
    
    for item in tqdm(data):
        if item['address'] == "":
            for row in schData:
                if item['fullname'] == row['fullname']:
                    item['address'] = row['address']
                    empty_row = empty_row -1
    
    print("Empty row %s" % str(empty_row))

    print('Processed')
    
    print("Empty addrs left: %s" % str(len([item for item in data if item['address'] == ""])))

    with open("all_school_data.json", "w") as jsonfile:
            json.dump(data, jsonfile)

def main():
    with open("SELECT_t___FROM_schools_ege_t.csv") as datafile:
        dataCSV = csv.DictReader(datafile)
        data = []
        for row in dataCSV:
            data.append(row)
        
            
        with open("SELECT_t___FROM_schools_subject_t.csv") as subjfile:
            subj = csv.DictReader(subjfile)
            for row in subj:
                for item in data:
                    if row['id'] == item['subject_id']:
                        item['subject'] = row['alias']
        data2 = []            
        with open("schools.csv") as addrfile:
            schools = csv.DictReader(addrfile)
            for row in schools:
                for item in data:
                    #print("%s %s" % (str(row['id']), str(item['school_id'])))
                    if str(row['id']) == str(item['school_id']):
                        print("Gotcha!")
                        z = item.copy()
                        print(z)
                        z.update(row)
                        data2.append(z)
                                
        with open("all_school_data.json", "w") as jsonfile:
            json.dump(data2, jsonfile)
            
                
            