from setuptools import setup


setup(
    name='fileMover', 
    version='1.0', 
    py_modules=['fileMover'], 
    install_requires=[
        'click'
    ], 
    entry_points='''
        [console_scripts]
    fileMover=fileMover:fileMover
    '''
)