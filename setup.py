'''
The setup.py file is used to define the package metadata and dependencies for a Python project.
It allows you to specify information such as the package name, version, author, description, and any required dependencies.
This file is essential for packaging and distributing your Python project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    try:
        requirement_lst:List[str] = []
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements!="-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    
    return requirement_lst

setup(
    name='networksecurity',
    version='0.0.1',
    author='Pushpesh Pant',
    author_email='pushpeshpant19@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)