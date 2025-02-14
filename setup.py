from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path: str):
    """
    Reads the requirements.txt file and returns a list of valid dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e")]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="fault_detection",  # Replace with your project name
    version="0.1.0",  # Version of your package
    # description="A brief description of your project",
    author="Ajit",
    author_email="ajitkumarbgs2003.com",
    # url="https://github.com/your_username/your_project",  # Repository URL
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=get_requirements('requirements.txt')

)
