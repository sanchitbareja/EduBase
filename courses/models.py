from django.db import models
 
# Create your models here.
class Course(models.Model):
	course_title = models.CharField(max_length=1000)
	course_start_date = models.DateField()
	course_end_date = models.DateField()

class Assessment(models.Model):
	ASSESSMENT_OPTIONS = (
		('M','midterm'),
		('H','homework'),
		('F','final'),
		('P','project'),
	)
	course = models.ForeignKey(Course)
	assessment_type = models.CharField(max_length=1000, choices=ASSESSMENT_OPTIONS)
	due_date = models.DateTimeField()
