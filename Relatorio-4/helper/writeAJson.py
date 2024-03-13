import json
import os
from bson import json_util  # pip install bson


def writeAJson(data, name: str):
    
    parsed_json = json.loads(json_util.dumps(data))
    print(f".")
    if not os.path.isdir("./json"):
        os.makedirs("./json")
        print(f"..")
        
    print(f"...")
    with open(f"./json/{name}.json", 'w') as json_file:
        print(f"....")
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))