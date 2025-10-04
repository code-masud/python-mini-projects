import csv
import json
from .base import Base

class CSVToJSON(Base):
    def purify_value(self, value):
        if value == '':
            return None

        true_values = ['true', 'yes', '1', 'on', 'y', 't', 'oui', 'si', 'ja']
        false_values = ['false', 'no', '0', 'off', 'n', 'f', 'non', 'nein']

        lower_value = value.lower()
        if lower_value in true_values:
            return True
        elif lower_value in false_values:
            return False

        try:
            if '.' in value or 'e' in lower_value or 'E' in lower_value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value

    def convert(self):
        try:
            with open('files/Book1.csv', newline='') as csv_file:
                data = [{key:self.purify_value(value) for key, value in row.items()} for row in csv.DictReader(csv_file)]
        except Exception as e:
            print(f"An error occurred while reading file: {e}")
        else:
            try:
                with open('files/data.json', 'w', newline='') as file:
                    json.dump(data, file, indent=4, sort_keys=False, separators=(",",":"), ensure_ascii=False)
            except Exception as e:
                print(f"An error occurred while writing file: {e}")
            else:
                print("CSV to JSON completed.")