from django import forms

from django.contrib.auth.models import User, Group
from django.forms.util import ErrorList
from django.forms import ModelForm
from datetime import date, timedelta, datetime
from models import Website

class WebsiteForm(forms.Form):
  """
  form for Website model 
  the naming for this model is consistent with bindmodels.py 

  """
  domain = forms.CharField(max_length=40)
  meta_key = forms.CharField(max_length=50, required=False)
  meta_desc = forms.CharField(widget=forms.Textarea, required=False)
  notes = forms.CharField(widget=forms.Textarea, required=False)
  
  
  def clean(self):
    return self.cleaned_data

  def save(self):
    """
    Save the website object
    """
    website = Website(**self.cleaned_data)
    website.save()
    

class WebsitePageForm(forms.Form):
  """
  form for Website model 
  the naming for this model is consistent with bindmodels.py 

  """
  website = forms.ModelChoiceField(queryset=Website.objects.all())
  title = forms.CharField(max_length=30)
  name = forms.CharField(max_length=20)
  type = forms.CharField(max_length=15)
  template = forms.CharField(max_length=50)
  redirects_to = forms.CharField(max_length=30)
  
  
  def clean(self):
    return self.cleaned_data

  def save(self):
    pass
