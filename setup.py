"""
Flask-GnuPG
--------------

Simple GnuPG wrapper for Flask applications.
"""
from setuptools import setup


setup(
    name='Flask-GnuPG',
    version='0.1',
    url='https://github.com/ics/Flask-GnuPG/',
    license='MIT',
    author='Alexandru Ciobanu',
    author_email='iscandr@gmail.com',
    description='Simple GnuPG wrapper for Flask applications',
    long_description=__doc__,
    zip_safe=False,
    packages=['flask_gnupg'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'python-gnupg>=0.3.8'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
