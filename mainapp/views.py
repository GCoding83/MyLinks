from django.shortcuts import render
from django.views.generic import DetailView, ListView
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


# Class-based views
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



