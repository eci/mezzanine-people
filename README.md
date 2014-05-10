Overview
========
This pluggable app provides a "Person" model to categorize and list people on your Mezzanine sites.


Requirements
============
[Mezzanine CMS] [1]


Setup
=====
* Add mezzanine_people to your environment:
```bash
    pip install mezzanine_people
```

* Add "mezzanine_people" to INSTALLED_APPS:
```python
    INSTALLED_APPS = (
        "...",
        "mezzanine_people",
    )
```

* Set values in your project settings.py (optional):
```python
    PEOPLE_PER_PAGE = 5 # the default is 10
```

* Include the people URLconf in your project urls.py like this:
```python
    url(r'^people/', include('mezzanine_people.urls')),
```

* Run `python manage.py createdb` or `python manage.py syncdb && python manage.py migrate`.


Releases
--------
+ Version 0.1 - Initial Release

[1]: http://mezzanine.jupo.org "Mezzanine CMS"
