# setup.py for unsloth - Fork of unslothai/unsloth
# Fast and memory-efficient LLM fine-tuning

from setuptools import setup, find_packages
import os

# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Core dependencies required for unsloth
INSTALL_REQUIRES = [
    "torch>=2.1.0",
    "transformers>=4.38.0",
    "datasets>=2.16.0",
    "sentencepiece>=0.1.99",
    "tqdm>=4.66.0",
    "psutil",
    "wheel>=0.42.0",
    "packaging>=23.1",
    "tyro>=0.7.2",
    "numpy",
    "accelerate>=0.28.0",
    "peft>=0.10.0",
    "bitsandbytes>=0.43.0",
    # NOTE: relaxed protobuf constraint - protobuf 4.x works fine in my testing
    "protobuf>=3.20.0",
    "huggingface_hub",
]

# Optional dependencies for extra features
EXTRAS_REQUIRE = {
    "vision": [
        "Pillow>=10.0.0",
        "torchvision",
    ],
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov",
        "black",
        "isort",
        "flake8",
        "mypy",
    ],
    "triton": [
        "triton>=2.1.0",
    ],
    "xformers": [
        "xformers>=0.0.23",
    ],
    # Personal addition: notebook extras I commonly use when experimenting
    "notebook": [
        "ipywidgets>=8.0.0",
        "ipython>=8.0.0",
        # Added matplotlib for quick loss curve plots during training runs
        "matplotlib>=3.7.0",
        # Added seaborn for nicer plots with minimal extra effort
        "seaborn>=0.13.0",
    ],
}

# Combine all optional deps under 'all'
EXTRAS_REQUIRE["all"] = [
    dep
    for group, deps in EXTRAS_REQUIRE.items()
    if group not in ("dev",)
    for dep in deps
]

setup(
    name="unsloth",
    version="2024.12.0",
    author="Unsloth AI",
    author_email="daniel@unsloth.ai",
    description="2x faster, 70% less memory LLM fine-tuning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://docs.unsloth.ai",
        "Source Code": "https://github.com/unslothai/unsloth",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    python_requires=">=3.9",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        "console_scripts": [
            "unslot
