from typing import List
from setuptools import find_packages,setup


HYPEN_E_DOT="-e ."
def Find_requirements(file_path:str)->List[str]:
    '''
    This function will install requirements
    '''
    requirements=[]
    with open("requirements.txt") as  f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            print(requirements)

            requirements.remove(HYPEN_E_DOT)

        return requirements




setup(
name="ML_PROJECT",
version="0.0.1",
author="Basavaraj",
author_email="basavaraj5281b@gmail.com",
packages=find_packages(),
install_requires=Find_requirements("requirements.txt")
)