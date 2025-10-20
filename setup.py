from setuptools import find_packages, setup
from typing import List



def get_requirements() -> List[str]:
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement != '' and requirement!= '-e .':
                    requirement_lst.append(requirement)

            return requirement_lst
        
    except FileNotFoundError:
        print("File having requirements Not Found")

    return requirement_lst

## print(get_requirements()) ## to check if the function is working as expected


setup (
    name= "Network_Security",
    version = '0.0.1' ,
    author= "SAMAAN LAMBE",
    install_requires = get_requirements(),
    packages= find_packages()
)