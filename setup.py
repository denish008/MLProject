from typing import List 
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """returns a list of requirements"""
    requirements = []
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "denish",
    author_email = "denishtrivedi008@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)