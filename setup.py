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
    description='https://github.com/Haoke98/saer-openapi-sdk',
    packages=["saer"],
    include_package_data=True,
    long_description=long_description,
    keywords=['saer', 'openapi', 'api', 'sdk', 'python-sdk', "api.isaerdata.com"],
    entry_points={
        'console_scripts': [

        ],
    },
)
