from django.shortcuts import render
from django.http import HttpResponse
# this is a temporary replacement for a database
class Board:  # Note that parens are optional if not inheriting from another class
  def __init__(self, brand, model, description, age):
    self.brand = brand
    self.model = model
    self.description = description
    self.age = age

boards = [
  Board('Burton', 'slayer', 'foul little demon', 3),
  Board('Lamar', 'slickBack', 'Degenerate myalopathy', 2),
  Board('k2', 'splice', 'really really not that bad', 6)
]
# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render (request, 'about.html')

def boards_index(request):
    return render(request, 'boards/index.html', {'boards': boards})