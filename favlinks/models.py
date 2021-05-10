from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    is_authorised = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=150)
    typel = models.CharField(default='1', max_length=1)

    # https://www.google.com/s2/favicons?domain=
    def __str__(self):
        return self.link
