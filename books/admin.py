from django.contrib import admin

# Register your models here.
from .models import Publish
from .models import Author
from .models import Book


class PublishAdmin(admin.ModelAdmin):

    list_display=('name', 'city', 'address')
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):

    list_display=('name', 'email', 'address', 'city', 'phone')


class BookAdmin(admin.ModelAdmin):

    list_display=('name', 'publication_date',)


admin.site.register(Publish, PublishAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
