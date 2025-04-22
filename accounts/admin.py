from django.contrib import admin
from .models import Category, Post, Author, PostCategory, Comment

# Register your models here.
# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['author', 'time_of_posting','title'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('author',  'time_of_posting')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title','time_of_posting' )  # тут всё очень похоже на фильтры из запросов в базу

class CategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['category_name'] # генерируем список имён всех полей для более красивого отображения

class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['user'] # генерируем список имён всех полей для более красивого отображения

class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['text_of_comment'] # генерируем список имён всех полей для более красивого отображения



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment,CommentAdmin)