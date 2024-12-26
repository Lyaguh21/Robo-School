from django.db import models


class registration_form(models.Model):
    user_email = models.EmailField(max_length= 20)
    user_password = models.TextField(max_length= 20)

    def __str__(self):
        return f"{self.user_email}"