from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('short_link', 'long_link', 'owner')


admin.site.register(Link, LinkAdmin)

