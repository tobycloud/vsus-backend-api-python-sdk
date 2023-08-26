from setuptools import find_packages, setup

with open("requirements.txt", "r", encoding="utf8") as file:
    install_requires = file.read().splitlines()

setup(
    name="backend_api",
    version="0.1.2",
    packages=find_packages(),
    install_requires=install_requires,
)
