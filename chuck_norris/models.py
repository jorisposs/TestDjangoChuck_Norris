from django.db import models


class Author(models.Model):
	author_name = models.CharField(max_length=50)
	author_lastname = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.author_name

class Quote(models.Model):
	joke_text = models.CharField(max_length=300)
	joke_author = models.ForeignKey(Author)
	
	def __unicode__(self):
		return self.joke_text
