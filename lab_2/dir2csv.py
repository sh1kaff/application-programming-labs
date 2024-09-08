import csv
import os

def dir2csv(dir, csv_name="some"):
    with open(csv_name + ".csv", "w", newline="") as csvfile:
        names = ("Rel. path", "Abs. path")

        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(names)

        for dirfile in os.listdir(dir):
            abs_path = os.path.abspath(dirfile)
            rel_path = os.path.relpath(abs_path, start=__file__)

            csv_writer.writerow((rel_path, abs_path))
            