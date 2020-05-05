# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-jdblackstar", # the name that you will install via pip
    version="1.1",
    author="Josh Black-Star",
    author_email="josh@blackstar.dev",
    description="A package containing 2 functions to filter dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jdblackstar/lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)