import setuptools

setuptools.setup()

## Can be used instead of static setup.cfg file. Optional.

#import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

#setuptools.setup(
#    name="BezoarIbex",
#    version="0.0.1",
#    author="Özgür Deniz Akyol",
#    author_email="dakyol@pm.me",
#    description="A python module for creating mathematical models of physical concepts.",
#    long_description=long_description,
#    long_description_content_type="text/markdown",
#    url="https://github.com/dakyol/BezoarIbex",
#    project_urls={
#        "Bug Tracker": "https://github.com/dakyol/BezoarIbex/issues",
#    },
#    classifiers=[
#        "Programming Language :: Python :: 3",
#        "License :: OSI Approved :: MIT License",
#        "Operating System :: OS Independent",
#    ],
#    package_dir={"": "src"},
#    packages=setuptools.find_packages(where="src"),
#    python_requires=">=3.6",
#)
