from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Forum, Chat, Pair, Comment, Resource, Goal, Category, BlogPost, User, Person, Questionnaire, Step



# Models registered here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    pass

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass

@admin.register(Goal)
class GoalBoardAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass