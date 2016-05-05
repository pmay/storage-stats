from setuptools import setup

setup(
    name='storage_characteriser',
    version='0.1',
    packages=['storage_characteriser'],
    url='',
    license='Apache 2',
    author='Peter May',
    author_email='Peter.May@bl.uk',
    description='Calculates count and average file size of files recorded by file extension',
    entry_points={
        'console_scripts': [
            'storage_characteriser = storage_characteriser.__main__:main'
        ]
    },
    install_requires=[
        "progressbar2"
    ]
)
