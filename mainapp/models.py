from django.utils.text import slugify
from django.db import models
from django.contrib import admin #For using the intermediary tables on the Admin page
from django.contrib.auth.models import User
from django.urls import reverse

#My two main classes, Publication and Author, have a many-to-many relationship. Publication types (articles, books, dissertations, etc.) inherit from Publication
class Publication(models.Model):
	ARTICLE = 'A'
	BOOK = 'B'
	BOOK_CHAPTER = 'C'
	DISSERTATION = 'D'
	STUDENT_WORK = 'S'
	PRESENTATION = 'P'
	WEB_PUBLICATION = 'W'
	OTHER_PUBLICATION_TYPE = 'O'
	PUB_TYPE = (
		(ARTICLE, 'Journal Article'),
		(BOOK, 'Book'),
		(BOOK_CHAPTER, 'Book Chapter'),
		(DISSERTATION, 'Dissertation'),
		(OTHER_PUBLICATION_TYPE, 'Other Publication Type'),
		(PRESENTATION, 'Presensation (Conference Talk, Course Lecture, etc.'),
		(STUDENT_WORK, 'Student Work (Other than Dissertation'),
		(WEB_PUBLICATION, 'Web Publication (Blog, etc.)'),)
	pub_type = models.CharField(max_length=1, choices=PUB_TYPE)
	author = models.ManyToManyField('Author', through='PublicationAuthor', related_name='publications')
	slug = models.SlugField(unique=True, default='')
	title = models.CharField(max_length=200)
	# For slugs
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Publication, self).save(*args, **kwargs)

	year = models.IntegerField()
	abstract = models.TextField(blank=True, null=True, help_text='You can enter the abstract later if you prefer.')
	journal = models.ForeignKey('Journal', on_delete=models.CASCADE, default='', null=True, blank=True)
	citation = models.ManyToManyField('self', through='CitationMetadata', through_fields=('citer_pub', 'cited_pub'), symmetrical=False, related_name='citations')
	# 
	def __str__(self):
		return str(self.title + ' (' + str(self.year) + ')' + ' - ' + self.pub_type + str(self.id))

	# To tell Django how to find the URL to any specific instance of a publication that we create
	def get_absolute_url(self):
		return reverse('publication-authors-new-page')


class Author(models.Model):
	slug = models.SlugField(unique=True, default='')
	first_name = models.CharField(max_length=30, blank=True, null=True, help_text='Optional. If author only has one name (e.g. Aristotle), enter it as a last name')
	middle_name = models.CharField(max_length=60, blank=True, null=True, help_text='Optional.')
	last_name = models.CharField(max_length=30, help_text='Required.')
	# For slugs
	def save(self, *args, **kwargs):
		self.slug = slugify(self.last_name)
		return super(Author, self).save(*args, **kwargs)

	# def get_absolute_url(self):

	# 	if self.middle_name == None:
	# 		if self.first_name == None:
	# 			kwargs = {'slug': self.slug}
	# 			return reverse('author-detail-last', kwargs=kwargs)
	# 		kwargs = {'slug': self.slug, 'first_name': self.first_name}
	# 		return reverse('author-detail-first-last', kwargs=kwargs)
	# 	elif self.first_name == None and self.middle_name:
	# 		kwargs = {'slug': self.slug, 'middle_name': self.middle_name}
	# 		return reverse('author-detail-middle-last', kwargs=kwargs)	
	# 	kwargs = {'slug': self.slug, 'first_name': self.first_name, 'middle_name': self.middle_name}
	# 	return reverse('author-detail-first-middle-last', kwargs=kwargs)
	
	def __str__(self):
		if self.middle_name == None:
			if self.first_name == None:
				return str(self.last_name)		
			return str(self.first_name) + ' ' + str(self.last_name)
		elif self.first_name == None and self.middle_name:
			return str(self.middle_name) + ' ' + str(self.last_name)
		return str(self.first_name) + ' ' + str(self.middle_name) + ' ' + str(self.last_name)

	# To tell Django how to find the URL to any specific instance of an author that we create
	def get_absolute_url(self):
		return reverse('author-detail-page', kwargs={'slug': self.slug, 'pk': self.pk})


#Intermediary table 
class PublicationAuthor(models.Model):
	author = models.ForeignKey('Author', related_name='publication_authors', on_delete=models.CASCADE)
	publication = models.ForeignKey('Publication', related_name='publication_authors', on_delete=models.CASCADE)
	author_rank = models.IntegerField(default=1)

	class Meta:
		ordering = ('publication', 'author_rank')
		unique_together = ('author', 'publication', 'author_rank')

	def __str__(self):
		return str(self.author) + ' in ' + str(self.publication.title)

	def get_absolute_url(self):
		return reverse('publications-page')

class PublicationAuthorInline(admin.TabularInline):
	model = PublicationAuthor
	extra = 1



#Citations have a one-to-many relationship with two distinct publications: the one that cites, and the one that is cited.
class CitationMetadata(models.Model):
	cited_pub = models.ForeignKey('Publication', related_name='cited_pubs', on_delete=models.CASCADE)
	citer_pub = models.ForeignKey('Publication', related_name='citer_pubs', on_delete=models.CASCADE)
	page_begin_in_citer = models.IntegerField(null=True, blank=True)
	page_end_in_citer = models.IntegerField(null=True, blank=True)
	page_begin_in_cited = models.IntegerField(null=True, blank=True)
	page_end_in_cited = models.IntegerField(null=True, blank=True)
	actual_citation = models.TextField(null=True, blank=True, default='No text for the citation is provided. Please see the citation Context.')
	citation_context = models.TextField(null=True, blank=True, default='No context is provided for this citation. Please see the citation text.')

	def __str__(self):
		return "Citer: " + self.citer_pub.title + '; Cited: ' + self.cited_pub.title

class CitationMetadataInline(admin.TabularInline):
	model = CitationMetadata
	extra = 1
	#Include the below for a recursive, M2M table.
	fk_name='citer_pub'

class PublicationAdmin(admin.ModelAdmin):
	inlines = (PublicationAuthorInline, CitationMetadataInline)



#Intermediary table 
# class PublicationCitation(models.Model):
# 	citation = models.ForeignKey('Citation', related_name='publication_citations', on_delete=models.CASCADE)
# 	citer = models.ForeignKey('Publication', related_name='publication_citations', on_delete=models.CASCADE)


# class PublicationCitationInline(admin.TabularInline):
# 	model = PublicationCitation
# 	extra = 1

# class PublicationAdmin(admin.ModelAdmin):
# 	inlines = (PublicationCitationInline,)




# #For now at least. the Journal class does not inherit from Publication, because it has no authors.
class Journal(models.Model):
	journal_name = models.CharField(max_length=200)
	volume = models.IntegerField()
	issue = models.IntegerField()
	year = models.IntegerField()
	academic_domain = models.CharField(max_length=100)
	page_total = models.IntegerField()

	def __str__(self):
		return self.journal_name + ', ' + str(self.volume) + '(' + str(self.issue) + ')'



#Below are all the types of publications that inherit from Publication. Each has an inline for the PublicationAuthor table
class Article(Publication):
	article_page_begin = models.IntegerField()
	article_page_end = models.IntegerField()
	# def __str__(self):
	# 	return '"' + self.title + '" in ' + self.journal.journal_name + ' (' + str(self.journal.year) + ')'

class ArticleAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]


class Dissertation(Publication):
	dissertation_page_total = models.IntegerField(null=True, blank=True)
	dissertation_chapter_total = models.IntegerField(null=True, blank=True)
	dissertation_university = models.CharField(max_length=150, null=True, blank=True)
	dissertation_university_department = models.CharField(max_length=150, null=True, blank=True)
	dissertation_supervisor = models.CharField(max_length=100, null=True, blank=True)

class DissertationAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]

class Book(Publication):
	publisher = models.CharField(max_length=200, null=True, blank=True, help_text='Optional.')
	book_page_total = models.IntegerField(null=True, blank=True, help_text='Optional.')
	book_chapter_total = models.IntegerField(null=True, blank=True, help_text='Optional.')

	def __str__(self):
		return self.title + ' (' + str(self.year) + ')' 

	# To tell Django how to find the URL to any specific instance of a publication that we create
	def get_absolute_url(self):
		return reverse('publication-authors-new-page')

class BookAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]

#BookChapter inherits from Publication and has a one-to-many relationship with Book.
class BookChapter(Publication):
	source_book = models.ForeignKey('Book', related_name='book_chapters', on_delete=models.CASCADE)
	chapter_number = models.IntegerField()
	chapter_page_begin = models.IntegerField()
	chapter_page_end = models.IntegerField()

	def __str__(self):
		return '"' + self.title + '" in ' + self.source_book.title + ' (' + str(self.source_book.year) + ')'

class BookChapterAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]


class Presentation(Publication):
	event_description = models.CharField(max_length=150)
	event_city = models.CharField(max_length=150)
	event_country = models.CharField(max_length=150)

class PresentationAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]


class StudentWork(Publication):
	work_context_description = models.CharField(max_length=150)

class StudentWorkAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline, 
		]


class WebPublication(Publication):
	url = models.URLField(max_length=200)
	website_description = models.CharField(max_length=200)

class WebPublicationAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline, 
		]

class OtherPublicationType(Publication):
	publication_type_description = models.CharField(max_length=100, null=True, blank=True)	

class OtherPublicationTypeAdmin(admin.ModelAdmin):
	inlines = [
		PublicationAuthorInline, CitationMetadataInline,
		]