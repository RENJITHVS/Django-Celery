from pathlib import Path
from django.http import HttpResponse
from .tasks import *


def generate_random_file(request, filename: str, dataCount: int):
    path = Path(f'data/{filename}.csv')
    if not path.is_file():
        generate_file.apply_async(args=[filename, dataCount])
        return HttpResponse("<h1> The CSV file generated successfully </h1>")
    else:
        return HttpResponse("<h1> The CSV file already exists </h1>")


def index(request):
    return HttpResponse(
        "<h1> Welcome </h1> <h2> please enter the filename and number of file to be generated on address bar </br> eg: http://127.0.0.1:8000/firstdata/16 </h2>"
    )
