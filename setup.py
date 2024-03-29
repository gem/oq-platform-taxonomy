import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='oq-platform-taxonomy',
    version='1.1',
#    packages=find_packages(),
    packages=["openquakeplatform_taxonomy"],
    include_package_data=True,
    license='BSD License',  # example license
    description='Taxtonomy - GEM building taxonomy glossary',
    long_description=README,
    url='http://github.com/gem/oq-platform-taxonomy',
    author='GEM Foundation',
    author_email='devops@openquake.org',
    install_requires=[
        'django >=4.2, <5',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Scientists',
        'License :: OSI Approved :: AGPL3',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
