from django import forms

from django.contrib.auth.models import User, Group
from django.forms.util import ErrorList
from django.forms import ModelForm
from datetime import date, timedelta, datetime
from models import Website, WebsitePage

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

  def update(self, obj):
    """
    Edit the object, pass the object too !
    """
    for k, v in self.cleaned_data.items():
      setattr(obj, k, v)
      obj.save()
      
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
  website = forms.ModelChoiceField(queryset=Website.objects.all(), required=False)
  title = forms.CharField(max_length=50)
  name = forms.CharField(max_length=20)
  type = forms.ChoiceField(choices=WebsitePage.PAGETYPES)
  template = forms.CharField(max_length=50)
  redirects_to = forms.CharField(max_length=30, required=False)
  
  
  def clean(self):
    return self.cleaned_data

  def save(self):
    if not self.cleaned_data.get('website'):
      self._errors = ErrorList(['Website is required'])
    else:
      websitepage = WebsitePage(**self.cleaned_data)
      websitepage.save()

  def update(self, obj):
    """
    we will skip the website when modifying to avoid any mistakes
    in leaving the entry blank
    """
    for k, v in self.cleaned_data.items():
      # skip website - delete the page if needed
      if not k == 'website':
        setattr(obj, k, v)
      obj.save()


