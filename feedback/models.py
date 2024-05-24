from django.db import models


class Feedback(models.Model):
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    name = models.TextField("Имя")
    email = models.EmailField("Почта", max_length=255)
    topic = models.TextField("Тема")
    message = models.TextField("Сообщение")

    def __str__(self) -> str:
        return "{} от {}".format(self.topic, self.name)

    class Meta:
        verbose_name = "Обратная связь пользователя"
        verbose_name_plural = "Обратная связь пользователей"
