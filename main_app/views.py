from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render (request, 'about.html')

  
def boards_index(request):
  boards = Board.objects.all()
  return render(request, 'boards/index.html',{'boards':boards})

def boards_details(request, board_id):
  board=Board.objects.get(id=board_id)
  return render(request, 'boards/detail.html', {'board': board})


