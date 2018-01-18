import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='syscrew-exchange',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='SysCrew License',
    description='AMQP wrapper to consume and publish events',
    long_description=README,
    url='https://www.syscrew.xyz/',
    author='Anas Aldrees',
    author_email='asaldrees@syscrew.xyz',
    install_requires=['kombu'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
