Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# -*- coding: utf-8 -*-
from django import forms



class HomeForm(forms.Form):
    num1 = forms.IntegerField(required=False)
    num2 = forms.IntegerField(required=False