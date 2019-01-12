import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rusyllab",
    version="0.0.1",
    author="Ilya Koziev",
    author_email="inkoziev@gmail.com",
    description="Simple Python 2/3 package for breaking Russian words into syllables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Koziev/rusyllab",
    packages=setuptools.find_packages(),
)