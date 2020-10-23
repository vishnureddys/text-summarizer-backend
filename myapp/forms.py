from django import forms 

# creating a form 
class InputForm(forms.Form): 
	article_name = forms.CharField(max_length=200)
