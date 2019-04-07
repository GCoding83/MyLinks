from django.urls import path 
from .views import AuthorDetailView, AuthorListView, HomeListView, PublicationDetailView, PublicationListView, BookListView
from . import views 

urlpatterns = [ 
	#Below is how you assign routes for function-based views 
	path('', HomeListView.as_view(), name='mainapp-home'), 
	path('about/', views.about, name='about-page'),

	# Below, for class-based views
	path('authors/', AuthorListView.as_view(), name='authors-page'),
	# Use variables to specify a distinct route per author
	#The generic class-based detail view EXPECTS to be passed a parameter named pk. If you're writing your own function view you can use whatever parameter name you like, or indeed pass the information in an unnamed argument.
	path('authors/<slug:slug>/<int:pk>/', AuthorDetailView.as_view(), name='author-detail-page'),
	path('publications/', PublicationListView.as_view(), name='publications-page'),
	path('publications/<slug:slug>/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-page'),
	path('books/', BookListView.as_view(), name='books-page'),
] 