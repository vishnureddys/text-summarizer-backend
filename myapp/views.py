from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import InputForm 
import wikipedia

# Create your views here. 
def home_view(request):
    if request.method == 'GET':
        form = InputForm()
    else:
        form = InputForm(request.POST)
        if form.is_valid():
            article_name = form.cleaned_data['article_name']
            get_data_from_wiki(article_name)
            return redirect('success')
    return render(request, 'home.html',{'form':form})

def successView(request):
    return render(request, 'temp.html')

def get_data_from_wiki(name):
    data = wikipedia.page(name)
    print(data.content)
    return