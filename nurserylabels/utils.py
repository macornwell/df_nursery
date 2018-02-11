import csv


def generate_nursery_front_label_csv(output, list_of_labels):
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['name', 'ripens', 'species'])
    for label in list_of_labels:
        data = [
            label.name,
            label.ripens,
            label.species
        ]
        writer.writerow(data)
