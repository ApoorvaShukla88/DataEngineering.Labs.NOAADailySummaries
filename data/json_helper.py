import json
import os
#import pickle
import pandas as pd

def read_json(file_path: str) -> Dict:
    with open(file_path) as f:
        json_input = json.load(f)
    return json_input

def read_all_json_files(JSON_ROOT):
    for dirpath, dirname, filenames in os.walk(JSON_ROOT):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(JSON_ROOT, f))
                for i in json_content['results']:
                    i['source'] = f
                    result.append(i)
    df_location = pd.DataFrame(result)
    return df_location