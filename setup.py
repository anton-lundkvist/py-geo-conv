import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygeoconv",
    version="1.0.0",
    author="Anton Lundkvist",
    author_email="antonlundkvist@gmail.com",
    description="Python tool for converting geometries between WKT, GeoJson and Esri Json formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anton-lundkvist/py-geo-conv",
    packages=setuptools.find_packages(exclude=('tests.*', 'tests', "tests*"), include=("pygeoconv*")),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[]
)
