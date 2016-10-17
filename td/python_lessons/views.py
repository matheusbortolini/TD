from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .users import UserForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Document, DocumentForm


class UserFormView(View):
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
        return render(request, 'registration.html', {'form': form})


def home(request):
    if request.user.is_authenticated():
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = Document(doc_file=request.FILES['doc_file'])
            new_doc.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            form = DocumentForm()
        documents = Document.objects.all()
        return render(request, 'home.html', {'documents': documents, 'form': form})
    return render(request, 'index.html')


def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('registration'))
    form = DocumentForm()
    documents = Document.objects.all()[0:2]
    return render(request, 'index.html', {'documents': documents, 'form': form})


class LogUser(View):
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'login.html', {'form': form})
