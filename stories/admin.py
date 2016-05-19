from django.contrib import admin
from .models import Story
# Register your models here.
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'domain', 'moderator', 'created',]
	list_filter = ['created', 'updated',]
	search_fields = ['title', 'moderator__username', 'moderator__last_name']
	fields = ['title', 'url', 'moderator',]


admin.site.register(Story, StoryAdmin)
