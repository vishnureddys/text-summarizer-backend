from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
#from .forms import InputForm 
from .forms import ArticleForm
from .models import Article

import wikipedia

#from .models import Article
def show_form(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article_name = form.cleaned_data['article_name']
        data = get_data_from_wiki(article_name)
        #TODO - Add this function
        #summary = summarize_data(data)
        article = Article.objects.create_article(article_name)
        article.data = data #TODO - make data as summary so that directly summary will be stored here instead of the whole data.
        article.save()
    return render(request,"home.html", {'form':form})

'''
def summarize_data(data):
    #TODO- By manikya
    #Just add your code here and check if it works
'''

def get_data_from_wiki(name):
    data = wikipedia.page(name)
    #print(data.content)
    return str(data.content)