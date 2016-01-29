# How to do the first exercise

We decided to include in this section the installation of djangostack and the installation of our new module.

## Installation

First we need to download [djangostack](https://bitnami.com/stack/django) from [bitnami](https://www.bitnami.org).

We have to go to the download folder and execute the file bitnami-djangostack\[...\].

In the process of installation, we are going to select MySQL as the only storage system (uncheck SQLite and Postgree). Of course, there's no harm if you want to install them. 

The setup process will ask us if we want to create an initial project. In our case is a *YES*. In my particular case, I called the project PyLadies.

At some point it will ask you if you want to allow incomming connections. This is to setup Apache, feel free to choose according to your security standards. Personally I said yes. This can be changed afterwards if needed.

In this project we will create our application (I decided to call it django_models).

Say yes to everything. For MySQL Root password, feel free to choose something convenient. Otherwise you can leave it blank.

## Activate django from command line

This gave us many headaches in our practice session because we didn't use it. Please USE IT.

My installation is on MacOS, the default installation directory is /Applications/djangostack\[...\]. On other OS, this directory may change. You can always check the directory with the stack's manager app.

We go to this defacult directory with the command line and execute ./use_djangostack. This will activate a pseudo virtual environment with the correct version of python, mysql, etc.

## Create our application

We assume we are parting from our stack's default directory. We need to go to \[stack_base\]/apps/django/django_projects/PyLadies. In this directory we will find a *manage.py* file (among others). We may execute
```bash
python manage.py startapp django_models
```

This will create a directory called "django_models" with some files inside.

## Create our model

We need to modify the file models from our brand new *django_models* directory.

We are going to build the following schema in our model

[insert image here]

We need to add the following:
```python

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

#From here on, is optional

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
```

## Install application and migrate model

Once we have our model created, we can *notify* django that a new application have been installed. To do so, we need to locate a file named **settings.py** in our Project folder *PyLadies*

We don't need to worry about the database configuration since the stack already did it for us. We need to add our application (django_models) to our INSTALLED_APP just like the following:
```python
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_models',
)
```

And once again, we need to use manage.py. Once we are in the same directory, we need to execute the following:
```bash
python manage.py makemigrations django_models
```

If this step doesn't show any errors, we can follow up with 
```bash
python manage.py migrate django_models
```

This second instruction will actually create the tables and his relationships in the database. The previous step is to generate the SQL instructions that's why it's very important to not have any error.

## Finished

Congratulations, you finished the first exercise. I hope you enjoyed. See you on the next one!