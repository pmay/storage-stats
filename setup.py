from setuptools import setup

setup(
    name='storagestats',
    version='0.1',
    packages=['storagestats'],
    url='',
    license='Apache v2',
    author='Peter May',
    author_email='Peter.May@bl.uk',
    description='Calculates count and average file size of files recorded by file extension',
    entry_points={
        'console_scripts': [
            'storagestats = storagestats.__main__:main'
        ]
    },
    install_requires=[
        "progressbar2"
    ]
)
