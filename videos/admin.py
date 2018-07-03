from django.contrib import admin

from .models import Video, Comment, Playlist

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class VideoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Video Information', {'fields': ['title', 'description']}),
        ('Files', {'fields': ['video_file', 'thumbnail']}),
        ('Details', {'fields': ['uploader', 'pub_date', 'listed']}),
    ]

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.created_by != request.user and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.created_by != request.user and not request.user.is_superuser:
            return False
        return True
    
    inlines = [CommentInline]

admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Video, VideoAdmin)