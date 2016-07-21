import os
from setuptools import setup
from djssoserver import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dj-sso-server2',
    version=__version__,
    packages=['djssoserver'],
    include_package_data=True,
    license='GPL v2.0',
    description='A Django SSO provider application',
    long_description=README,
    url='https://github.com/tofu0913/dj-sso-server',
    author='Fan Fei, Cliff Chen',
    author_email='tofu0913@gmail.com',
    install_requires=['dj-api-auth',],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
