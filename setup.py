from setuptools import setup, find_packages

# Read the requirements from requirements.sh
with open("requirements.sh") as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="passmanager",
    version="1.0.0",
    author="M S Praveen Kumar",
    author_email="mspraveenkumar77@gmail.com",
    description="A simple password manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=required,
    # entry_points={
    #     "console_scripts": [
    #         "securepassmanager = passwordmanager.securepassmanager:main",
    #     ]
    # },
)
