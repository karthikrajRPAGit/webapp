from setuptools import find_packages, setup

setup(
    name="webapp",
    version="0.0.3",
    package_dir={"":"app"},
    packages=find_packages(where="app"),
    install_requires=["flask","requests"],
    python_requires=">=3.6",
)