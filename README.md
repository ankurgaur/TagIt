TagIt
=====

A system to store your bookmarks along with tags to make it easier to search.

You need to make some changes to `settings.py` in order to make the app work.
- Add the following declaration to make the templates work:
```
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)
```
- Change the `DATABASES` to make it look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<YOUR_MYSQL_DATABASE_NAME>',
        'USER': '<YOUR_MYSQL_USER_NAME>',
        'PASSWORD': '<YOUR_MYSQL_USER_PASSWORD>',
        'HOST': '',
        'PORT': '',
    }
}
```

- Add TagItApp to the INSTALLED_APPS.
