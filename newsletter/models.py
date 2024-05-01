from django.db import models
from django.contrib.auth.models import User


# Contact form for newsletter.
class NewsletterSignUp(models.Model):
    """
    Contact form for users to sign up to the newsletter
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name