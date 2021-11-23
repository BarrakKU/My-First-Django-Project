from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print(f"Request: {request}")

    name = "Barrak"

    return HttpResponse(f"""<html><body>
  <h1>Hello {name}!</h1>
  <p>This is my first <strong>html</strong> web app!</p>
  </body></html>""")