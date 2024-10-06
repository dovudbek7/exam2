from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class News(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    view_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sphere_of_activity = models.TextField()
    education = models.TextField()
    scientific_degree = models.TextField()
    legal_practice = models.TextField()
    license = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
    languages = models.TextField()
    image = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True)

class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Review(models.Model):
    service_id = models.IntegerField()
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    file = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Service(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    image = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    view_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)