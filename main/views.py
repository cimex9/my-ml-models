from django.shortcuts import render
from django.contrib import messages

from .utils import titanic_model as _titanic_model
from .utils.mnist_database_model import preprocess_image, predict_mnist_model


def index(request):
    return render(request, 'index.html')


def titanic_model(request):
    if request.method == 'GET':
        pclass = request.GET.get("Pclass")
        gender = request.GET.get("gender")
        age = request.GET.get("Age")
        fare = request.GET.get("Fare")

        gender = 1 if gender == 'Male' else 0 if gender == 'Female' else gender

        try:
            result = _titanic_model.predict([[pclass, gender, age, fare]])
            result = str(bool(result[0]))

            messages.add_message(request, messages.INFO, result)

        except ValueError:
            pass
    return render(request, 'models/titanic_model.html')


def mnist_database(request):
    probabilities = None
    if request.method == 'POST':
        base64_encoded_image = request.POST.get("imgPath")
        pixel_map = preprocess_image(base64_encoded_image)
        prediction, probabilities = predict_mnist_model(pixel_map)

        messages.add_message(request, messages.INFO, prediction)

    return render(request, 'models/mnist_database_model.html', {"probabilities": probabilities})
