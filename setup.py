from setuptools import setup, find_packages

setup(
    name='weather',
    version='0.0.1',
    description='Python tool to find the weather',
    author='Eric Cheatham',
    packages=find_packages('./weather'),
    include_package_data=True,
    install_requires=[
        'flask',
        'requests[security]',
    ],
    entry_points={
        'console_scripts' : ['weather = weather.cli:main']
    }
)
