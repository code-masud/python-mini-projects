import json
import csv
from .base import Base

class JSONToCSV(Base):
    def convert(self):
        try:
            with open('files/data.json', 'r', newline='') as file:
                data = json.load(file)
                if not data or not isinstance(data, list):
                    raise ValueError("JSON data should be a non-empty list")

                if not all(isinstance(item, dict) for item in data):
                    raise ValueError("All items in JSON list should be dictionaries")

                fieldnames = list(data[0].keys())
        except Exception as e:
            print(f"An error occurred while reading file: {e}")
        else:
            try:
                with open('files/Book2.csv', 'w', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)
            except Exception as e:
                print(f"An error occurred while writing file: {e}")
            else:
                print("JSON to CSV Completed")