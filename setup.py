# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/3/2
@Software: PyCharm
@disc:
======================================="""
"""
The build/compilations setup
>> pip install -r requirements.txt
>> python setup.py install
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = open('README.md').read()

setup(
    name='saer-openapi',
    url='https://github.com/Haoke98/saer-openapi-sdk',
    author='Haoke98',
    author_email='Haoke98@outlook.com',
    license='Apache2.0',
    description='https://github.com/Haoke98/saer-openapi-sdk',
    packages=["saer"],
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator"
    ],
    keywords=['saer', 'openapi', 'api', 'sdk', 'python-sdk', "api.isaerdata.com"],
    entry_points={
        'console_scripts': [

        ],
    },
)
