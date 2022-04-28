from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Binding, Board
from .forms import TuningForm
import uuid
import boto3
from .models import Board, Binding, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector1'

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

def boards_detail(request, board_id):
  board = Board.objects.get(id=board_id)
  bindings_board_doesnt_have = Binding.objects.exclude(board = board.bindings.all().values_list('id'))
  tuning_form = TuningForm()
  return render(request, 'boards/detail.html', {'board': board, 'tuning_form': tuning_form})

def add_tuning(request, board_id):
  form = TuningForm(request.POST)
  if form.is_valid():
    new_tuning = form.save(commit=False)
    new_tuning.board_id = board_id 
    new_tuning.save()
  return redirect('detail', board_id=board_id)

def assoc_binding(request, boards_id, binding_id):
  Board.objects.get(id=boards_id).binding.add(binding_id)

def add_photo(request, board_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, board_id=board_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', board_id=board_id)