from setuptools import setup, find_packages
import sys, os

setup(
    name='app_folder_name',
    version='0.1',
    description="Django app",
    long_description=open('README.md', 'r').read(),
    keywords='',
    author='',
    author_email='',
    url='',
    license='MIT',
    package_dir={'app_folder_name': 'app_folder_name'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
