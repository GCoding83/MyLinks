from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
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

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['journal', 'title', 'year', 'article_page_begin','article_page_end', 'abstract']

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'year', 'publisher', 'book_page_total','book_chapter_total', 'abstract']

class JournalCreateView(LoginRequiredMixin, CreateView):
    model = Journal;
    fields = ['journal_name', 'volume', 'issue', 'year', 'page_total']

class PublicationFirstStep(forms.Form):
    BOOK = 'B'
    ARTICLE = 'A'
    JOURNAL = 'J'
    VOLUME_CHAPTER = 'C'
    DISSERTATION = 'D'
    STUDENT_WORK = 'S'
    PRESENTATION = 'P'
    WEB_PUBLICATION = 'W'
    OTHER_PUBLICATION_TYPE = 'O'
    PUB_TYPE = (
        (BOOK, 'Book'),
        (ARTICLE, 'Article'),
        (JOURNAL, 'Journal'),
        (VOLUME_CHAPTER, 'Volume Chapter'),
        (DISSERTATION, 'Dissertation'),
        (STUDENT_WORK, 'Student Work (Other than Dissertation)'),
        (PRESENTATION, 'Presentation (Conference Talk, Course Lecture, etc.)'),
        (WEB_PUBLICATION, 'Web Publication (Blog, Online Encyclopedia, etc.)'),
        (OTHER_PUBLICATION_TYPE, 'Other Publication Type'),
        )
    publication_type = forms.ChoiceField(choices=PUB_TYPE, label="Please specify the publication type")
def publication(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublicationFirstStep(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if form.cleaned_data['publication_type'] == 'A':
                return redirect('article-new-page')
            elif form.cleaned_data['publication_type'] == 'B':
                return redirect('book-new-page')
            elif form.cleaned_data['publication_type'] == 'J':
                return redirect('journal-new-page')    
            else:
                return redirect('publications-new-page')

                         
    #If the request is not a POST, it will just render an empty form
    else:
        form = PublicationFirstStep()
    # if a GET  we'll create a blank form
    return render(request, 'mainapp/publication_first_step.html', {'form': form})

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


# class PublicationAuthorForm(ModelForm):
#     class Meta:
#         model = PublicationAuthor
#         publication =
class PublicationAuthorCreateView(LoginRequiredMixin, CreateView):
    # form_class = 
    model = PublicationAuthor
    fields = ['publication', 'author', 'author_rank']

    def get_initial(self):
        publication = Publication.objects.get(pk=self.kwargs['pk'])
        return {'publication': publication}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    # #     # publication = Publication.objects.get(pk=kwargs['pk'])
    #     # context['form'] = PublicationAuthorForm(initial={'publication': publication})
    #     publication = Publication.objects.get(pk=79)
    #     mynum = 5
    #     context['test'] = PublicationAuthorCreateView(initial={'author_rank': mynum})
    #     # context['test'] = publication

    #     return context
  
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



