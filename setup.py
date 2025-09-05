from setuptools import setup

setup(
    name="plsens",
    version="0.1",
    py_modules=["plsens"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "plsens = plsens.__main__:main"
        ],
    },
)