from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    #Перечесление полей пост
    list_display = ("text", "pub_date", "author")
    #Добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    #Фильтрация по дате
    list_filter = ("pub_date", )
# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)