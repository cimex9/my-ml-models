from django.shortcuts import render
from django.contrib import messages

from .utils import model


def index(request):
    return render(request, 'index.html')


def titanic_model(request):
    #                        UI
    if request.method == 'GET':
        pclass = request.GET.get("Pclass")
        sex = request.GET.get("Sex")
        age = request.GET.get("Age")
        fare = request.GET.get("Fare")

        sex = 1 if sex == 'Male' else 0 if sex == 'Female' else sex

        try:
            result = model.predict([[pclass, sex, age, fare]])
            result = str(bool(result[0]))

            messages.add_message(request, messages.INFO, result)

        except ValueError:
            pass
    return render(request, 'models/titanic_model.html')
