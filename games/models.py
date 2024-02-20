from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    released_date = models.DateField()
    character = models.TextField()
    preview_image = models.ImageField(upload_to='game_preview_image/')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    triller_url = models.CharField(max_length=100, blank=True, null=True)
    downloaded = models.IntegerField(default=0)
    size = models.CharField(max_length=50)
    file = models.FileField(upload_to='game_torrent_file/')
    gener = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class GameScreenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_screenshot_image/')

    def __str__(self):
        return str(self.game)


class GameReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.game}"

