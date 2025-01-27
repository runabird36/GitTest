import json
import pandas as pd

concert_info = {
                "name": "Rockin' Road Trip",
                "location": "New York City",
                "date": "July 4, 2023",
                "bands":
                    [
                        {
                            "name": "The Rolling Stones",
                            "genre": "rock",
                            "songs":
                                [
                                    {
                                        "title": "Satisfaction",
                                        "duration": 233,
                                    },
                                    {
                                        "title": "Gimme Shelter",
                                        "duration": 272,
                                    },
                                    {
                                        "title": "Jumpin' Jack Flash",
                                        "duration": 220,
                                    },
                                ],
                        },
                        {
                            "name": "The Black Keys",
                            "genre": "rock",
                            "songs":
                                [
                                    {
                                        "title": "Lonely Boy",
                                        "duration": 204,
                                    },
                                    {
                                        "title": "Howlin' For You",
                                        "duration": 210,
                                    },
                                    {
                                        "title": "Gold on the Ceiling",
                                        "duration": 223,
                                    },
                                ],
                        },
                        {
                            "name": "Kendrick Lamar",
                            "genre": "hip-hop",
                            "songs":
                                    [
                                        {
                                            "title": "HUMBLE.",
                                            "duration": 177,
                                        },
                                        {
                                            "title": "DNA.",
                                            "duration": 185,
                                        },
                                        {
                                            "title": "Alright",
                                            "duration": 307,
                                        },
                                ],
                        },
                    ],
                }



def convert_realInfo_into_str(info):
    """convert input information into string type value
        this function is desinged to save the list or dict type of data into dataframe

    Args:
        info (list or dict): real information and the type of it is list or dict

    Returns:
        str : converted information
    """
    return json.dumps(info)

def convert_str_into_realInfo(serialized_info):
    """convert the converted information into real information

    Args:
        serialized_info (str): converted information

    Returns:
        list or dict : real information
    """
    return json.loads(serialized_info)

def create_table(default_info :dict) -> pd.DataFrame:
    """Create dataframe type of table from dictionary
    """
    return pd.DataFrame(default_info)

class ConcertInfoController():
    def __init__(self, _name, _location, _date, _bands):
        self.name       = _name
        self.location   = _location
        self.date       = _date
        self.bands      = _bands

    def save_information_into_database(self):
        """
        1. convert list type of bands information into dataframe type of bands information
        2. and then save it in excel file or other file format
        """
        pass






# =======================================================
# This is an example regarding how to use convert list or
# dict type of information into string type value
# =======================================================
real_info = [
                {
                    "title": "Satisfaction",
                    "duration": 233,
                },
                {
                    "title": "Gimme Shelter",
                    "duration": 272,
                },
                {
                    "title": "Jumpin' Jack Flash",
                    "duration": 220,
                },
            ]


converted_info = convert_realInfo_into_str(real_info)
print(converted_info)
print(type(converted_info))

real_info_from_str = convert_str_into_realInfo(converted_info)
print(real_info_from_str)
print(type(real_info_from_str))
