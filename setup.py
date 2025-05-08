
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    repo_name="MadeDesignEasy",  # name of your package
    version="0.1.0",     # version of your package
    packages=find_packages(),  # automatically finds all packages/modules
    install_requires=[
        # Optional: list dependencies here instead of requirements.txt
    ],
    url=f"https://github.com/{author_user_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    author_user_name="sumitrwk90",
    author_email="sumitrwk@gmail.com",
    description="An end to end ML design project.",
    long_description=long_description
)
