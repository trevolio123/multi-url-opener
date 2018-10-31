if __name__ == "__main__":

    import csv
    with open('multi-url-opener - test CSV.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in rows:
            print(row, 0)