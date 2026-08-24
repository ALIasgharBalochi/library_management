from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    pages = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateField()
    category = models.ManyToManyField(Category)
