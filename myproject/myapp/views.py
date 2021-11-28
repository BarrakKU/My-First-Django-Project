from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print(f"Request: {request}")

    name = "Barrak"
    age = 20

    c = {}
    c["name"] = name
    c["age"] = age

    return render(request, "test.html", c)