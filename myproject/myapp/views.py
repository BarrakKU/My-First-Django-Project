from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print(f"Request: {request}")

    name = request.GET.get("username")
    age = 20
    major = "MIS"
    majors = [
        "MIS", 
        "Finance",
        "Accounting",
        "Management",
        "OM",
        "Marketing",
        "Public Administration"
        ]

    c = {}
    c["name"] = name
    c["age"] = age
    c["major"] = major
    c["majors"] = majors

    return render(request, "test.html", c)

def greet_view(request, u=None, a=None):
    
    p = {
        "username":u,
        "age":a,
    }

    return render(request, "greet2.html")