import setuptools
import bottle_restx

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bottle-restx",
    version=bottle_restx.__version__,
    author=bottle_restx.__author__,
    #author_email="author@example.com",
    description="A simple resource based REST API extension for the bottle framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bliepp/bottle-restx",
    project_urls={
        "Bug Tracker": "https://github.com/bliepp/bottle-restx/issues",
    },
    py_modules=['bottle_restx'],
    #scripts=['bottle_restx.py'],
    #packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)