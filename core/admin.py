from django.contrib import admin
from core.models import Forum, Comment, Resource, VisionBoard, Category, ProgressTracker, BlogPost

# Models registered here.
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass

@admin.register(VisionBoard)
class VisionBoardAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(ProgressTracker)
class ProgressTrackerAdmin(admin.ModelAdmin):
    pass