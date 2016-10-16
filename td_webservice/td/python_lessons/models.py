from django.db import models
from django import forms


class Document(models.Model):
    doc_file = models.FileField()


class DocumentForm(forms.Form):
    doc_file = forms.FileField(label='Upload de arquivo')