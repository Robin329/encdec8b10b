import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='encdec8b10b',
    version='1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/Robin329/encdec8b10b',
    license='MIT',
    author='Renbin.jiang',
    author_email='jiangrenbin123@gmail.com',
    description='8B10B Encoding and Decoding',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
