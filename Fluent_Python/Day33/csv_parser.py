import csv


def parse_parts(csv_filename):
    with open(csv_filename, encoding="utf-8") as partscsv:
        reader = csv.reader(partscsv)
        return [row[0] for row in reader]


def parse_inventory(csv_filename):
    with open(csv_filename, newline="") as qbinventorycsv:
        reader = csv.reader(qbinventorycsv, delimiter=",")

        # This skips the header
        next(qbinventorycsv)

        # on a list, grab the item in index, or return ___ as a default
        return [
            {"description": row[0], "availability": int(row[7]) if row[7] else 0}
            for row in reader
        ]






parts = parse_parts()
inventory = parse_inventory()
# Define a function
def marry_the_data(parts, inventory):

    # Create an empty List
    results = []

    # Iterator over parts
    # Where is parts from?????
    for part in parts:
        # Iterate over inventory
        # Where is inventory from????
        for item in inventory:

            # Once we get each item from the inventory
            # if the description starts with the part name
            # but doesn't end in PC or B
            # Add that part to the Results
            if (
                item["description"].startswith(part)
                and not item["description"].startswith(part + "-PC")
                and not item["description"].startswith(part + "-B")
            ):
                results.append(
                    {
                        "part": part,
                        "description": item["description"],
                        "availability": item["availability"],
                    }
                )

    # Return Results
    return results


def save_csv():
    # write out to a new csv
    with open("inventory.csv", "w", newline="") as output:
        writer = csv.writer(output, delimiter=",")
        for result in results:
            writer.writerow(
                [result["part"], str(max(0, min(result["availability"], 20)))]
            )

