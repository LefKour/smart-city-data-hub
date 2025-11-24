import requests
from config import Config

class CarbonExtractor:
    def __init__(self):
        self.base_url = Config.CARBON_API_BASE_URL

    def get_regional_data_by_postcode(self, postcode):
        url_postcode = postcode.replace(" ", "")
        endpoint = f"{self.base_url}/regional/postcode/{url_postcode}"
        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json()
            data["region_postcode"] = postcode
            return data
        else:
            return None

    def get_regional_data_by_region_id(self, region_id: int):
        endpoint = f"{self.base_url}/regional/regionId/{region_id}"
        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json()
            data["region_id"] = region_id
            return data
        else:
            return None

    def get_london_data(self):
        results = {
            "london_regions": [],
            "london_postcodes": []
        }

        for region_id in Config.LONDON_REGION_IDS:
            data = self.get_regional_data_by_region_id(region_id)
            if data is not None:
                results["london_regions"].append(data)

        for postcode in Config.LONDON_POSTCODES:
            data = self.get_regional_data_by_postcode(postcode)
            if data is not None:
                results["london_postcodes"].append(data)

        return results