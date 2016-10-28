import json
from tqdm import tqdm

def main():
    with open('web/crimstat.js') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            for key in [ttt for ttt in item.keys() if ttt !='name' and ttt != 'upperdistrict']:
                if item[key]:
                    try:
                        item[key] = item[key].replace(' ', '')
                    except:
                        pass
                    try:
                        item[key]= int(item[key])
                    except:
                        pass
        with open('web/crimstat2.js', "w") as savefile:
            json.dump(data, savefile)