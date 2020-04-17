from django.db import models

class CoreMember(models.Model) :
	fullname = models.TextField()
	college = models.TextField()
	branch = models.TextField()
	categories = models.TextField()	# string of numbers seperated by ','
									# 1 - communication, 2 - web, 3 - outreach, 4 - something else, ...
