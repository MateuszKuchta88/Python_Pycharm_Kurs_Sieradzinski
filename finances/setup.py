from setuptools import setup, find_packages

setup(name='finances',
      version='0.0.1',
      description='some description',
      long_description='some long description',
      author='Mateusz Kuchta',
      author_email='kuchta.mateusz88@gmail.com',
      url='https://pystart.pl',
      packages=find_packages(exclude=['tests', '*.tests']))
