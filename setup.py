from setuptools import find_packages, setup

with open("requirements.txt", "r", encoding="utf8") as reqs:
    install_requires = reqs.read().splitlines()

setup(
    name="backend_api",
    version="0.1.9",
    packages=find_packages(),
    package_data={
        "backend_api": ["*.pyi"],
    },
    install_requires=install_requires,
)
