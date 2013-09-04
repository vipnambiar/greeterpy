from setuptools import setup

with open('README.rst') as file_descriptor:
    long_description = file_descriptor.read()

setup(
    name='Greeter',
    version='0.1.dev1',
    packages=['greeter',],
    license='Apache License 2.0',
    long_description=long_description,
    package_data={ 
                  '': ['README*', 'LICENSE', '*.txt', '*.rst'], 
                  },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={ 'console_scripts' : ['greet = greeter.greet:main',] },
)
