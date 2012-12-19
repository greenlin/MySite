from setuptools import setup

setup(name='MySite',
      version='1.0',
      description='OpenShift App',
      author='Green Lin',
      author_email='lin.green@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
                        'Flask',
                        'Flask-FlatPages'
                        ],
#      install_requires=['Django>=1.3'],
     )
