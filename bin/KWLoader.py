import os 
import sys
import json


def get_keywords_for(language):
    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
    else:
        app_path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{app_path}/data/{language}.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)["keywords"][0]

    KEYWORDS = [
        data_dict['var'],
        data_dict['and'],
        data_dict['or'],
        data_dict['not'],
        data_dict['if'],
        data_dict['elif'],
        data_dict['else'],
        data_dict['from'],
        data_dict['to'],
        data_dict['step'],
        data_dict['while'],
        data_dict['func'],
        data_dict['do'],
        data_dict['end'],
        data_dict['return'],
        data_dict['continue'],
        data_dict['break'],
    ]

    return data_dict, KEYWORDS