from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'read_on'
    list_display = ('title', 'isbn', 'read_on', 'notes')

admin.site.register(Book, BookAdmin)
