import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyppca",
    version="0.0.5",
    author="Ludvig Hult",
    author_email="ludvig.hult@gmail.com",
    description="Probabilistic PCA with Missing Values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/el-hult/pyppca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     install_requires = [
      'numpy',
      'scipy',
    ],
)
