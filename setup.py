from setuptools import find_packages, setup

long_description = "\n".join(
    (
        open("README.rst", encoding="utf-8").read(),
        open("CHANGES.txt", encoding="utf-8").read(),
    )
)

setup(
    name="more.jinja2",
    version="0.4.dev0",
    description="Jinja2 template integration for Morepath",
    long_description=long_description,
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    keywords="morepath jinja2",
    license="BSD",
    url="https://github.com/morepath/more.jinja2",
    namespace_packages=["more"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=["setuptools", "morepath >= 0.15", "Jinja2 >= 2.9"],
    extras_require=dict(
        test=["pytest >= 7", "pytest-cov", "WebTest"],
        lint=[
            "black == 23.9.1",
            "flake8 == 6.1.0",
            "pyupgrade == 3.14.0",
            "isort == 5.12.0",
        ],
    ),
)
