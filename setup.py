from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='teknofile',
    authoer_email='teknofile@teknofile.org',
    description='A utility for backup up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/teknofile/pgbackup',
    packages=find_packages('src')
)
