from setuptools import setup

setup(
    name='storage-stats',
    version='0.1',
    packages=['storage_stats'],
    url='',
    license='Apache v2',
    author='Peter May',
    author_email='Peter.May@bl.uk',
    description='Calculates count and average file size of files recorded by file extension',
    entry_points={
        'console_scripts': [
            'storage_stats = storage_stats.__main__:main'
        ]
    },
    install_requires=[
        "progressbar2"
    ]
)
