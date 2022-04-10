import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from main.utils import titanic_model


def api_redirect(request):
    return redirect('docs')


def documentation(request):
    return render(request, 'api/docs.html')


class TitanicAPI(View):
    def get(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            data = {"message": "Invalid JSON schema!"}
            return JsonResponse(data, status=400)

        pclass = data.get('pclass')
        sex = data.get('sex')
        age = data.get('age')
        fare = data.get('fare')

        sex = 1 if sex == 'male' else 0 if sex == 'female' else sex

        if (pclass not in range(1, 4)) or \
                (sex not in [1, 0]) or \
                (age not in range(100)) or \
                (not (0 <= fare <= 1000)):

            data = {"message": "Invalid JSON schema!"}
            return JsonResponse(data, status=400)

        result = titanic_model.predict([[pclass, sex, age, fare]])
        result = bool(result[0])
        return JsonResponse({"survived": result}, status=200)
