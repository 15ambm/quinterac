from setuptools import setup

setup(
    name='Quinterac',
    version='0.1',
    py_modules=['frontend'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=frontend:hello
    ''',
)