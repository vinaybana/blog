from django.contrib import admin
from .models import Post, Category, Tag, Comment


class postAdmin(admin.ModelAdmin):
	
	view_on_site = True
	fieldsets = [
		(None, {'fields': ['title', 'text', 'author', 'tag', 'category', 'slug', 'cmnt']}),
		('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'author', 'published_date', 'created_date')
	list_filter = ['published_date']
	search_fields = ['title']
	filter_horizontal = ('tag',)


admin.site.register(Post,postAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)


# Register your models here.
