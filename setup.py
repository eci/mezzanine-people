from setuptools import setup, find_packages
import os
import mezzanine_people

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine-people',
    version=mezzanine_people.__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple People app for Mezzanine CMS sites.',
    long_description=README,
    url='https://github.com/eci/mezzanine-people',
    author='Doug Evenhouse',
    author_email='doug.evenhouse@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
