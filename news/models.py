from django.db import models


class Post(models.Model):
    title = models.TextField("Заголовок")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    views = models.IntegerField("Просмотры", default=0)
    likes = models.IntegerField("Количество понравившихся", default=0)
    content = models.TextField("Содержимое")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Новостной пост"
        verbose_name_plural = "Новостные посты"
