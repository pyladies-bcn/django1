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


