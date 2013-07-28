from distutils.core import setup

with open('README.md') as file_descriptor:
    long_description = file_descriptor.read()

setup(
    name='Greeter',
    version='0.1.dev1',
    packages=['greeter',],
    license='Apache License 2.0',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)