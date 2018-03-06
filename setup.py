from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Python package to manage users on a server based on an “inventory” JSON file.'
    long_description=readme,
    author='Arseni Dudko',
    author_email='arseni_dudko@mail.ru',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
        )

