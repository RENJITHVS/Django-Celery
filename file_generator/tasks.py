import csv
import random
from celery import shared_task

NAMES = ["Kiran", "Arun", "Megha", "Jeeva", "Azar", "Abid", "Simon"]
CITIES = ["Delhi", "Kolkata", "Chennai", "Mumbai", "Kochi", "Banglore", "Pune"]


@shared_task(bind=True)
def generate_file(self, filename: str, dataCount: int):
    fieldnames = ["id", "name", "age", "city"]
    writer = csv.DictWriter(open(f"data/{filename}.csv", "w"), fieldnames=fieldnames)
    for i in range(0, dataCount):
        writer.writerow(
            dict(
                [
                    ("id", i + 1),
                    ("name", random.choice(NAMES)),
                    ("age", str(random.randint(10, 30))),
                    ("city", random.choice(CITIES)),
                ]
            )
        )
    return "Done"
