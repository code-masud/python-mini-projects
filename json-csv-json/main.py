from models import CSVToJSON, JSONToCSV

def demonstrate_operation():
    csv_to_json = CSVToJSON('files/Book1.csv', 'files/data.json')
    csv_to_json.convert()

    json_to_csv = JSONToCSV('files/data.json', 'files/Book2.csv')
    json_to_csv.convert()


def main():
    try:
        demonstrate_operation()
    except Exception as e:
        print(f'An error occurred: {e}')
        return 1
    return 0

if __name__ == '__main__':
    exit(main())