from setuptools import setup, find_packages

setup(
    name='nsf_next_launch_scraper',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'requests',
        'python-dotenv',
        'boto3'
    ]
)
