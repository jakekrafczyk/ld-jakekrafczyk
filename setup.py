from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ld-jakekrafczyk", # the name that you will install via pip
    version="2.0",
    author="Jake Krafczyk",
    author_email="jacob-krafczyk@lambdastudents.com",
    description="A data science tool kit",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jakekrafczyk/ld-jakekrafczyk",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)