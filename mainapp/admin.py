from django.contrib import admin
# from .models import Book, BookAdmin, BookChapter, BookChapterAdmin, OtherPublicationType, OtherPublicationTypeAdmin, Presentation, PresentationAdmin, StudentWork, StudentWorkAdmin, WebPublication, WebPublicationAdmin
# from .models import Article, ArticleAdmin, Author, Citation, Dissertation, DissertationAdmin, Journal, Presentation, PresentationAdmin
from .models import Article, ArticleAdmin, Author, Book, BookAdmin, BookChapter, BookChapterAdmin, Dissertation, DissertationAdmin, Journal, OtherPublicationType, OtherPublicationTypeAdmin, Presentation, PresentationAdmin, Publication, PublicationAdmin, StudentWork, StudentWorkAdmin, WebPublication, WebPublicationAdmin

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Dissertation, DissertationAdmin)
admin.site.register(Journal)

admin.site.register(Publication, PublicationAdmin)


admin.site.register(Book, BookAdmin)
admin.site.register(BookChapter, BookChapterAdmin)
admin.site.register(OtherPublicationType, OtherPublicationTypeAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(StudentWork, StudentWorkAdmin)
admin.site.register(WebPublication, WebPublicationAdmin)









