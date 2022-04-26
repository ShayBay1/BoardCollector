from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Board

class BoardCreate(CreateView):
  model = Board
  fields = '__all__'

class BoardUpdate(UpdateView):
  model = Board
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class BoardDelete(DeleteView):
  model = Board
  success_url = '/boards/'


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


