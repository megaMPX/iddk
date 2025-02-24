from django.contrib import admin
from .models import News, Image, Audio, SliderImage, About, Authors, Editors, Readers  # Импортируйте новые модели

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Количество пустых форм для добавления новых изображений

class AudioInline(admin.TabularInline):
    model = Audio
    extra = 1  # Количество пустых форм для добавления новых аудио

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'reader', 'published_date', 'book_type', 'is_published', 'book_code')
    search_fields = ('title', 'author', 'reader')
    list_filter = ('book_type', 'is_published')
    inlines = [ImageInline, AudioInline]
    fields = ('title', 'content', 'author', 'reader', 'book_type', 'likes', 'dislikes', 'published_date', 'is_published', 'book_code')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('content',)

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('content',)

class EditorsAdmin(admin.ModelAdmin):
    list_display = ('content',)

class ReadersAdmin(admin.ModelAdmin):
    list_display = ('content',)

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Editors, EditorsAdmin)
admin.site.register(Readers, ReadersAdmin)