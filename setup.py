from setuptools import setup, find_packages

# Read the contents of your README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code_reviewer",
    version="1.0.0",
    author="Pavel Erokhin",
    author_email="pavel.v.erokhin@gmail.com",
    description="An AI-powered code review bot that analyzes Git diffs and checks coherence with issues.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pavelerokhin/code_reviewer",
    packages=find_packages(where="."),
    package_dir={"": "."},
    install_requires=[
        "openai",
        "python-dotenv",
        "setuptools",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Version Control",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "code_reviewer=code_reviewer.main:main",
        ],
    },
    include_package_data=True,
    keywords="AI code review Git OpenAI GPT",
    license="MIT",
)
