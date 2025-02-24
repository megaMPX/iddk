from django.db import models

class News(models.Model):
    TEXT = '📖 Бумага'
    EBOOK = '📱Текст'
    AUDIO = '🎧Аудио'
    BOOK_TYPE_CHOICES = [
        (TEXT, 'Бумажная книга'),
        (EBOOK, 'Электронная книга'),
        (AUDIO, 'Аудиокнига'),
    ]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.CharField(max_length=100, default='Неизвестный автор')  # Установите значение по умолчанию
    reader = models.CharField(max_length=100, blank=True, null=True)  # Новое поле для чтеца
    book_type = models.CharField(max_length=20, choices=BOOK_TYPE_CHOICES, default=TEXT)  # Новое поле для типа книги
    is_published = models.BooleanField(default=True)  # Новое поле для статуса публикации
    book_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.news.title}"

class Audio(models.Model):
    news = models.ForeignKey(News, related_name='audios', on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return f"Audio for {self.news.title}"


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class About(models.Model):
    content = models.TextField()  # Поле для хранения текста о вас

    def __str__(self):
        return "Информация о нас"
    


class Authors(models.Model):
    content = models.TextField()  # Поле для хранения текста о авторах

    def __str__(self):
        return "Информация для авторов"

class Editors(models.Model):
    content = models.TextField()  # Поле для хранения текста о редакторах

    def __str__(self):
        return "Информация для редакторов"

class Readers(models.Model):
    content = models.TextField()  # Поле для хранения текста о читателях

    def __str__(self):
        return "Информация для читателей"