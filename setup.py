import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roboparse",
    version="0.0.2",
    author="Kel0",
    author_email="rozovdima123@gmail.com",
    description="Roboparse HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Toffooo/roboparser",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "lxml==4.6.3",
        "beautifulsoup4==4.9.3",
    ]
)
