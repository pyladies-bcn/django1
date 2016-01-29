# Exercise 2: How to

This part of the exercise is pretty simple and easy but not least tricky. Please read carefully

## Download sample database

First of all, we need to download django_models_testDB.zip

Note that for this exercise, we assumed your application is called "django_models". Otherwise, you may need to modify exployees_personalized.sql and change all ocurrences of "django_models_soemthing" for "your_app_name_something". Keep the "something" unchanged, thank you :)

## Load data

Well... this is the most complicated part. There are several ways to do so. We are going to see 2:
1. Use Django MySQL User
2. Use MySQL Root User

Of couse, the first option is better. The second one is less secure :P

### Django MySQL User

We can find this user and password in our project's settings.py file. Under the dictionary *DATABASES* you can find the user and the password. User is usually bitnami and the password varies.

Once we know those two values, we may proceed with the following:
```bash
mysql -u bitnami -p djangostack < employees_personalized.sql
```
The next step is to enter bitnami's password.

If everything goes well, our tables may be populated with lots of data to play in the next exercise

### MySQL Root User

Root user has the power to do anything so using this profile to manipulate our database is a bit dangerous. But it should be fine as long as we don't do anything inappropiate

The process is similar but in this case, the username is *root* and the password is the one we introduced when we did the installation.

So... we are going to type the following in the terminal:
(if you placed a password)
```bash
mysql -u root -p djangostack < employees_personalized.sql
```
(without password)
```bash
mysql -u root djangostack < employees_personalized.sql
```

After this, remember to grant permissions to bitnami user just in case it got lost :)

## Finishing up

If no errors have shown yet, you're done with this second exercise. Congratulations, you're closer to the final!