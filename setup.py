from setuptools import setup, find_packages

setup(
    name="mars_rover_project",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "app = app:cli",
        ],
    },
)
