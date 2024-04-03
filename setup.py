from setuptools import find_packages,setup
from typing import  List

HYPE_E_DOT = '-e.'

def get_requirement(file_path):
    requirement = []
    with open (file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [rep.replace("\n","")for rep in requirement]

        if HYPE_E_DOT in requirement:
            requirement.remove(HYPE_E_DOT)
    return  requirement
