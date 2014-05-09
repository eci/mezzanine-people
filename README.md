Overview
========
This pluggable app provides a "Person" model to categorize and list people on your Mezzanine sites.


Requirements
============
Required
    - [Mezzanine CMS] [1]


Installation
============
1. Add mezzanine_people to your virtualenv or clone the repository :
```bash
    pip install mezzanine_people
```

2. Add "people" to INSTALLED_APPS:
```python
    INSTALLED_APPS = (
        "...",
        "mezzanine_people",
    )
```

3. Set values for some settings (Optional):
```python
    PEOPLE_PER_PAGE = 5 # the default is 10
```

4. Include the people URLconf in your project urls.py like this:
```python
    url(r'^people/', include('mezzanine_people.urls')),
```

5. Run `python manage.py createdb` or `python manage.py syncdb && python manage.py migrate`.


Template Tag Usage
==================
1. Include people_tags in the template:

    {% load ... people_tags %}

2. Insert tag anywhere in the template:

    {% get_random_people 10 as featured_people_list %}


Version 0.1
-----------
    - Initial Release

[1]: http://mezzanine.jupo.org "Mezzanine CMS"
