from django.shortcuts import render
from .models import *

#publications = [
#    {
#        'id': 'B123',
 #       'lastname': 'Bradley',
  #      'fullname': 'Bradley, Ben',
   #     'title': 'Two Concepts of Intrinsic Value',
    #    'year': 2006,
     #   'pubtype': 'Article',
       # 'journalname': 'Ethical Theory and Moral Practice',
      #  'journalinfo': None,
        #'booknameifchapter': None,
        #'publisher': None,
        #'abstract': 'Recent literature on intrinsic value contains a number of disputes about the nature of the concept...',
        #'citations': [
        #				{
        #				'id': 'M001',
        #				'rank': 1,
        #				'lastname': 'Moore',
        #				'fullname': 'Moore, G. E.',
        #				'year': 1903,
        #				'title': 'Principia Ethica',
        #				'pubtype': 'Book',
        #				'journalname': None,
        #				'journalinfo': None,
        #				'bookname-ifchapter': None,
        #				'publisher': None,
        #				'relation': "Bradley presents Moore's book as being on the 'Moorean side' of the debate about the nature of the concept of intrinsic value."
        #				},
        #				{	
        #				'id': 'R001',
        #				'rank': 2,
        #				'lastname': 'Ross',
        #				'fullname': 'Ross, W.D.',
        #				'year': 1930,
        #				'title': 'The Right and the Good',
        #				'pubtype': 'Book',
        #				'journalname': None,
        #				'journalinfo': None,
        #				'bookname-ifchapter': None,
        #				'publisher': None,
        #				'relation': "Bradley presents this publication as being on the 'Moorean side' of the debate about the nature of the concept of intrinsic value."
  		#		    	}
  		#		    ]
  	#},
    
    ##   'id': 'Z123',
       # 'lastname': 'Ziff',
    #    'fullname': 'Ziff, Paul',
     #   'title': "On H.P. Grice's Account of Meaning",
      #  'year': 1967,
       # 'pubtype': 'Article',
    #    'journalname': 'Analysis',
     #   'journalinfo': None,
      #  'bookname-ifchapter': None,
    #   # 'publisher': None,
    #    'abstract': "Author criticizes Grice's account of meaning...",
     #   'citations': [
      #  				{	
       # 				'id': 'G001',
        #				'rank': 1,
        #				'lastname': 'Grice',
        #				'fullname': 'Grice, H. P.',
        #				'year': 1957,
        #  				'title': 'Meaning',
        # 				'pubtype': 'Article',
        # 				'journalname': 'Philosophical Review',
        # 				'journalinfo': "Vol.66 (3), 377-388",
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Reference to Grice's most relevant work for the present article."
        # 				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 2,
        # 				'lastname': 'Whorf',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 1956,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 3,
        # 				'lastname': 'Rawls',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 2001,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        #				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 4,
        # 				'lastname': 'Smith',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 2016,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        #				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 5,
        # 				'lastname': 'Thompson',
        # 				'fullname': 'Whorf, B.',
        #				'year': 1974,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 6,
        # 				'lastname': 'Adams',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 2000,
        # 				'title': 'Language, Thought, and Reality',
        #				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        #				{	
        # 				'id': 'W001',
        # 				'rank': 7,
        # 				'lastname': 'Giroux',
        # 				'fullname': 'Whorf, B.',
        #				'year': 2003,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{	
        # 				'id': 'W001',
        #				'rank': 8,
        # 				'lastname': 'Young',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 2015,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{    	
        #				'id': 'W001',
        # 				'rank': 9,
        # 				'lastname': 'Federer',
        #				'fullname': 'Whorf, B.',
        # 				'year': 2018,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        # 				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        # 				{	
        # 				'id': 'W001',
        # 				'rank': 10,
        # 				'lastname': 'Dude',
        # 				'fullname': 'Whorf, B.',
        # 				'year': 2004,
        # 				'title': 'Language, Thought, and Reality',
        # 				'pubtype': 'Book',
        # 				'journalname': None,
        # 				'journalinfo': None,
        #				'bookname-ifchapter': None,
        # 				'publisher': None,
        # 				'relation': "Grice cites Whorf only for a clarification about the phonetic significance of one of his (Grice's) examples"
        # 				},
        			
        #			]
    #}
#]

def home(request):
	context = {
          'publications': Publication.objects.all(),
		  'articles': Article.objects.all(),
          'authors': Author.objects.all(),
          'dissertations': Dissertation.objects.all(),
          'journals': Journal.objects.all(),
          'books': Book.objects.all(),
          'chapters': BookChapter.objects.all(),
          'citations': CitationMetadata.objects.all(),
          'othertypes': OtherPublicationType.objects.all(),
        'presentations': Presentation.objects.all(),
        'publicationauthors': PublicationAuthor.objects.all(),
         'studentworks': StudentWork.objects.all(),
             'webpubs': WebPublication.objects.all()
	} 
	return render(request, 'mainapp/mainapp-home.html', context)

def about(request):
	return render(request, 'mainapp/about.html')
