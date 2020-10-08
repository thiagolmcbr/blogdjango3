from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'sub_title', 'full_name', 
        'categories', 'Approved'
    ]
    search_fields = ['title', 'sub_title', 'content']
    
    def get_queryset(self, request):
        return Post.objects.filter()
admin.site.register(Post, PostAdmin)