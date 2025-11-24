from extract import CarbonExtractor
from transform import CarbonTransformer
from pymongo import MongoClient
from config import Config


if __name__ == '__main__':
    extractor = CarbonExtractor()
    raw_data = extractor.get_london_data()

    transformer = CarbonTransformer()

    all_records = []

    for region_data in raw_data["london_regions"]:
        records = transformer.transform_regional_data(region_data)
        all_records.extend(records)

    for postcode_data in raw_data["london_postcodes"]:
        records = transformer.transform_regional_data(postcode_data)
        all_records.extend(records)

    # Loader
    client = MongoClient(Config.MONGODB_URI)
    db = client[Config.MONGODB_DATABASE]
    collection = db[Config.MONGODB_COLLECTION]

    collection.insert_many(all_records, ordered=False)


