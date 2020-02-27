import setuptools

__version__ = '0.4.3'

packages = ['sharepoint',
            'sharepoint.lists']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sharepoint-eth-its",
    version=__version__,
    author="IT Services, University of Oxford",
    author_email="opendata@oucs.ox.ac.uk",
    maintainer='Graham Pugh',
    maintainer_email='g.r.pugh+github@gmail.com',
    description="Module and command-line utility to get data out of SharePoint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eth-its/python-sharepoint",
    packages=packages,
    scripts=['bin/sharepoint'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['SharePoint'],
    install_requires=['lxml', 'six'],
)