from datetime import datetime

class CarbonTransformer:
    def __init__(self):
        pass

    def parse_datetime(self, datetime_str: str):
        if datetime_str.endswith('Z'):
            datetime_str = datetime_str[:-1] + "+00.00"
        return datetime.fromisoformat(datetime_str)

    def calculate_renewable_percentage(self, generation_mix):
        renewable_sources = ["wind", "solar", "hydro", "biomass"]
        total = sum(item['perc'] for item in generation_mix if item['fuel'] in renewable_sources)
        return round(total, 2)

    def transform_regional_data(self, raw_data):
        records = []

        for data_item in raw_data.get("data", []):
            from_time = self.parse_datetime(data_item.get("from"))
            to_time = self.parse_datetime(data_item.get("to"))

            generation_mix = data_item.get("generationmix", [])

            record = {
                "from": from_time,
                "to": to_time,
                "region_id": data_item.get("region_id", ""),
                "postcode": data_item.get("postcode", ""),
                "renewable_percentage": self.calculate_renewable_percentage(generation_mix),
            }

            records.append(record)

        return records
