from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag_name

class Link(models.Model):
    link_url = models.URLField()
    link_tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.link_url

class User(models.Model):
    user_email = models.EmailField()
    user_password = models.CharField(max_length=40)     # SHA1 is represented as 40 characters
    user_links = models.ManyToManyField(Link)

    def __unicode__(self):
        return self.email
