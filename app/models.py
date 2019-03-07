from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Model of blog entry"""

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
