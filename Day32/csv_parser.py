import csv

def parse_parts(csv_filename):
    with open(csv_filename, encoding="utf-8") as partscsv:
        reader = csv.reader(partscsv)
        return [ row[0] for row in reader ]


def parse_inventory(csv_filename):
    with open(csv_filename, newline='') as qbinventorycsv:
        reader = csv.reader(qbinventorycsv, delimiter=',')

        # This skips the header
        next(qbinventorycsv)

        # on a list, grab the item in index, or return ___ as a default
        return [ {
            'description': row[0],
            'availability': int(row[7]) if row[7] else 0
        } for row in reader ]


# marry the data
def marry_the_data():
    results = []
    for part in parts:
        for item in inventory:
            if item['description'].startswith(part) and not item['description'].startswith(part + '-PC')  and not item['description'].startswith(part + '-B'):
                results.append({
                    'part': part,
                    'description': item['description'],
                    'availability': item['availability']
                })
    return results

def save_csv():
    # write out to a new csv
    with open('inventory.csv', 'w', newline='') as output:
        writer = csv.writer(output, delimiter=',')
        for result in results:
            writer.writerow([ result['part'], str(max(0, min(result['availability'], 20))) ])




# parts = parse_parts()
# inventory = parse_inventory()
