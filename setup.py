from setuptools import setup, find_packages

setup(
    name="spotify-playlist-transfer",
    version="0.1.0",
    description="Add your description here",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.13",
    install_requires=[
        "keyring>=25.6.0",
        "loguru>=0.7.3",
        "python-dotenv>=1.0.1",
        "questionary>=2.1.0",
        "rich>=13.9.4",
        "setuptools>=75.8.2",
        "spotipy>=2.25.1",
        "typer>=0.15.2",
    ],
    entry_points={
        "console_scripts": [
            "spotify-transfer=spotify_playlist_transfer.cli:app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
