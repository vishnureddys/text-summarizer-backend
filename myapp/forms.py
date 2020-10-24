from django import forms 
from .models import Article
# creating a form 
class ArticleForm(forms.ModelForm):
	article_name = forms.CharField()
	class Meta:
		model = Article
		fields = ['article_name',]


'''

class ArticleForm(forms.Form):
	class Meta:
		model = Article
		fields = ["article_name"]
class InputForm(forms.Form): 
	article_name = forms.CharField(max_length=200)
'''