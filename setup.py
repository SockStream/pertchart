from setuptools import setup

# read the contents of your README file
from os import path
work_dir = path.abspath(path.dirname(__file__))
with open(path.join(work_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pertchart',
  packages = ['pertchart'],
  version = '0.0.1',
  license='MIT',
  description = 'chart generator for "Livres Dont Vous Etes le Héros"',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'SockStream',
  author_email = '',
  url = 'https://github.com/SockStream/pertchart',
  keywords = ['pert chart', 'project plan', 'LDVEH'],
  install_requires=[
          'graphviz'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
