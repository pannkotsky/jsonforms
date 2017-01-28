from django.contrib import admin

from .models import Posting


@admin.register(Posting)
class PostingAdmin(admin.ModelAdmin):
    list_display = ('title', )
