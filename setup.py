import os

from setuptools import find_packages, setup

with open("requirements.txt", "r", encoding="utf8") as reqs:
    install_requires = reqs.read().splitlines()

data_files = [
    "backend_api/" + file for file in os.listdir("backend_api") if file.endswith(".pyi")
]

setup(
    name="backend_api",
    version="0.1.7",
    packages=find_packages(),
    data_files=[("backend_api", data_files)],
    install_requires=install_requires,
)
