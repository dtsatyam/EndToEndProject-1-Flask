from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements.txt
    """
    requirements = []
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name = "End to End ML Project with Flask Deployment",
    version = "0.0.1",
    author = "Satya",
    author_email = "dt.satyam@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)