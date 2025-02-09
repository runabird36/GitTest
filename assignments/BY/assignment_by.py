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
       
        main_info_dict = {"name":[], "genre":[], "songs":[]}
        for _band in self.bands:
            band_name = _band.get("name")
            band_genre = _band.get("genre")
            band_songs = _band.get("songs")
            main_info_dict["name"].append(band_name)
            main_info_dict["genre"].append(band_genre)
            main_info_dict["songs"].append(band_songs)
        
        updated_table = create_table(main_info_dict)
        print(updated_table)
        updated_table.to_excel(excel_writer="C:/dev/testtest.xlsx", sheet_name="TY")


# 1. save concert information from concert_info variable to ConcertInfoController Class
# 2. after executing some logic, want the function to save it into excel
# 3.

concert_name    = concert_info.get("name")
concert_loc     = concert_info.get("location")
concert_date    = concert_info.get("date")
concert_bands   = concert_info.get("bands")

maint_concert_controller = ConcertInfoController(concert_name, concert_loc, concert_date, concert_bands)

maint_concert_controller.save_information_into_database()







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


# converted_info = convert_realInfo_into_str(real_info)
# print(converted_info)
# print(type(converted_info))

# real_info_from_str = convert_str_into_realInfo(converted_info)
# print(real_info_from_str)
# print(type(real_info_from_str))
