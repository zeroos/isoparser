from setuptools import setup


setup(
    name='isoparser',
    version='0.2',
    author='Barney Gale',
    author_email='barney@barneygale.co.uk',
    url='https://github.com/barneygale/isoparser',
    license='MIT',
    description='Parser for the ISO 9660 disk image format',
    packages=["isoparser"],
    install_requires=["six"],
    test_suite="isoparser.test",
)
