import base64
import json
import binascii
import io

from PIL import Image

from django.shortcuts import render
from django.contrib import messages

from .utils import titanic_model


def index(request):
    return render(request, 'index.html')


def titanic_model(request):
    if request.method == 'GET':
        pclass = request.GET.get("Pclass")
        sex = request.GET.get("Sex")
        age = request.GET.get("Age")
        fare = request.GET.get("Fare")

        sex = 1 if sex == 'Male' else 0 if sex == 'Female' else sex

        try:
            result = titanic_model.predict([[pclass, sex, age, fare]])
            result = str(bool(result[0]))

            messages.add_message(request, messages.INFO, result)

        except ValueError:
            pass
    return render(request, 'models/titanic_model.html')


def mnist_database(request):
    result = "1"
    if request.method == 'POST':
        result = request.POST.get("imgPath").replace("data:image/jpeg;base64,", "")
        result = io.BytesIO(base64.b64decode(result))

        image = Image.open(result).convert("L")
        image = image.resize((28, 28))
        pixel_map = list(map(lambda x: round(x/255, 5), [x for x in image.getdata()]))
        result = pixel_map

        # messages.add_message(request, messages.INFO, result)

    return render(request, 'models/mnist_database_model.html', {"result": result})
