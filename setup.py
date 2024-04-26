from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="srai-docker-control",
    packages=find_packages(),
    version="0.1.1",  # TODO manual....
    license="",
    package_data={},
    python_requires=">=3.10",
    install_requires=requirements,
    author="Jaap Oosterbroek",
    author_email="jaap.oosterbroek@southriverai.com",
    description=".",
    entry_points={},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/southriverai/srai-docker-control",
    download_url="https://github.com/southriverai/srai-docker-control/archive/v_01.tar.gz",
    keywords=["AI"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
