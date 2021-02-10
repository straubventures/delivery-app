import csv

# Create a distance matrix
def load_distances(self):
    with open("WGUPS Distance Table clean.csv") as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        distances = []
        for row in readCSV:
            distances.append(row)
        return distances

