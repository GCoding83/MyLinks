from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView, 
    DetailView, 
    ListView,
    UpdateView
)
from django.views.generic.edit import ModelFormMixin
from .models import *

# Function-based views
# def home(request):
# 	context = {
#           'publications': Publication.objects.all(),
# 		  'articles': Article.objects.all(),
#           'authors': Author.objects.all(),
#           'dissertations': Dissertation.objects.all(),
#           'journals': Journal.objects.all(),
#           'books': Book.objects.all(),
#           'chapters': BookChapter.objects.all(),
#           'citations': CitationMetadata.objects.all(),
#           'othertypes': OtherPublicationType.objects.all(),
#         'presentations': Presentation.objects.all(),
#         'publicationauthors': PublicationAuthor.objects.all(),
#          'studentworks': StudentWork.objects.all(),
#              'webpubs': WebPublication.objects.all()
# 	} 
# 	return render(request, 'mainapp/mainapp-home.html', context)

def about(request):
	return render(request, 'mainapp/about.html')

# Class-based views
class AuthorListView(ListView):
    # This tells our ListView what model to querry in order to create the list.
    model = Author
    context_object_name = 'authors'
    #Note: the '-' sign indicates a reverse order. 
    #Note that if you enter an ordering value that is not valid, the error message in the browser will indicate the valid options to you.
    # ordering = ['-last_name']

class AuthorDetailView(DetailView):
    model = Author
    # Don't forget "query_pk_and_slug" if you intend to use both in the url
    slug_field = "slug"
    slug_url_kwarg = "slug"
    query_pk_and_slug = True

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'middle_name', 'last_name']


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    # Don't forget "query_pk_and_slug" if you intend to use both in the url
    slug_field = "slug"
    slug_url_kwarg = "slug"
    query_pk_and_slug = True
    #Where to redirect users after deletion
    success_url = '/'

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'middle_name', 'last_name']
    #This function works with UserPassesTestMixin to ensure that only people with the right permissions can update

class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    fields = ['title', 'year', 'pub_type']

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     for author in form.cleaned_data['author']:
    #         pubauth = PublicationAuthor()
    #         pubauth.publication = self.object
    #         pubauth.author = author
    #         pubauth.save()
    #     return super(ModelFormMixin, self).form_valid(form)

class PublicationAuthorCreateView(LoginRequiredMixin, CreateView):
    model = PublicationAuthor
    fields = ['publication','author']

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     for author in form.cleaned_data['author']:
    #         pubauth = PublicationAuthor()
    #         pubauth.publication = self.object
    #         pubauth.author = author
    #         pubauth.save()
    #     return super(ModelFormMixin, self).form_valid(form)

class PublicationListView(ListView):
    # This tells our ListView what model to querry in order to create the list.
    model = Publication
    context_object_name = 'publications'
    # ordering = ['-year']

class PublicationDetailView(DetailView):
    model = Publication
    # Don't forget "query_pk_and_slug" if you intend to use both in the url
    slug_field = "slug"
    slug_url_kwarg = "slug"
    query_pk_and_slug = True

class HomeListView(ListView):
    # This tells our ListView what model to querry in order to create the list.
    model = Publication
    # Specify the template to use. If nothing is specified, it goes for <app>/<model>_<viewtype>.html 
    template_name = 'mainapp/mainapp-home.html'
    context_object_name = 'publications'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    ordering = ['-year']



