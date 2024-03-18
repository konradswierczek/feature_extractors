from setuptools import find_packages, setup

setup(
    name="feature_extractors",
    version="1.1",
    author="Konrad Swierczek",
    author_email="swierckj@mcmaster.ca",
    description="Music content analysis audio feature extractors used throughout my PhD.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10.12",
    install_requires=["librosa == 0.10.0.post2", "essentia == 2.1b6.dev1110", 
                      "numpy == 1.24.2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/konradswierczek/feature_extractors",
    project_urls={
        "Homepage": "https://github.com/konradswierczek/feature_extractors",
        "Issues": "https://github.com/konradswierczek/feature_extractors/issues",
    },
    packages=find_packages(),
)