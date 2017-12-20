# -*- coding: utf-8 -*-

from itertools import chain
from setuptools import setup, find_packages
import xml.etree.ElementTree as ElementTree

try: # Try importing requests first.
    import requests
except ImportError:
    try: # Try importing Python3 urllib
        import urllib.request
    except AttributeError: # Now importing Python2 urllib
        import urllib

def get_content(url):
    try:  # Using requests.
        return requests.get(url).content # Returns requests.models.Response.
    except NameError:
        try: # Using Python3 urllib.
            with urllib.request.urlopen(index_url) as response:
                return response.read() # Returns http.client.HTTPResponse.
        except AttributeError: # Using Python3 urllib.
            return urllib.urlopen(url).read() # Returns an instance.

# Retrieve the legacy data and path.
index_url = 'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml'
len_url = len('https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/')
nltk_index = ElementTree.fromstring(get_content(index_url)).find('packages')
data_paths = {package.attrib['id']:[package.attrib['url'][len_url:]] for package in nltk_index.findall('package')}

requires = ['nltk']

setup(
  name = 'nltk_data_all',
  packages = find_packages(),
  version = '0.0.1',
  description = 'Unofficial Python Package for All NLTK Data.',

  package_data={'nltk_data_all':list(chain(*data_paths.values()))},

  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
    ],

    keywords = ['NLP', 'CL', 'natural language processing',
            'computational linguistics', 'parsing', 'tagging',
            'tokenizing', 'syntax', 'linguistics', 'language',
            'natural language', 'text analytics'],
)
