from setuptools import find_packages,setup


HYPE_E_DOT = '-e.'

def get_requirement(file_path):
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rep.replace("\n","")for rep in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return  requirements


setup(
    name ='MlProject',
    version='0.0.1',
    author='ashwanth',
    author_email='ashwantheee07@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirements.txt')
    )