from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView





from app1.models import Ques
# Create your views here.


class QList(ListView):
	model = Ques
	context_object_name = 'ques'



class QDetail(DetailView):
	model = Ques
	context_object_name = 'que'



