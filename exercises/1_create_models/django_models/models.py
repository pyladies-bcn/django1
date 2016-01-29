from django.db import models

# Create your models here.
class employees(models.Model):
	GENDER = (("M", "Male"), ("F", "Female"))
	empl_no = models.IntegerField(primary_key=True)
	birthdate = models.DateField()
	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=16)
	gender = models.CharField(max_length=1, choices=GENDER)
	hire_date = models.DateField()

class departments(models.Model):
	dept_no = models.CharField(max_length=4, primary_key=True)
	dept_name = models.CharField(max_length=40, unique=True)

class dept_emp(models.Model):
	emp_no = models.ForeignKey('employees')
	dept_no = models.ForeignKey('departments')
	from_date = models.DateField()
	to_date = models.DateField()

	class Meta:
		unique_together = (('emp_no', 'dept_no'))

class dept_manager(models.Model):
	emp_no = models.ForeignKey('employees')
	dept_no = models.ForeignKey('departments')
	from_date = models.DateField()
	to_date = models.DateField()

	class Meta:
		unique_together = (('emp_no', 'dept_no'))

class salaries(models.Model):
	emp_no = models.ForeignKey('employees')
	salary = models.IntegerField()
	from_date = models.DateField(primary_key=True)
	to_date = models.DateField()

class titles(models.Model):
	emp_no = models.ForeignKey('employees')
	title = models.CharField(max_length=50)
	from_date = models.DateField()
	to_date = models.DateField()

	class Meta:
		unique_together = (('title', 'from_date'),)
