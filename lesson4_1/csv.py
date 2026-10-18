import csv
from os import write

with open("user_csv.csv","w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "email", "role"])
    writer.writerow(["Lev","lev@gm.com","QA"])
    writer.writerow(["Ivan","ivan@gm.com","dev"])