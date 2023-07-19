import setuptools
import khmernormalizer

with open("README.md", "r") as f:
  readme_md = f.read()
    
setuptools.setup(
  name="khmernormalizer",
  version=khmernormalizer.__version__,
  description="A missing toolkit for Khmer Natural Language Processing.",
  long_description=readme_md,
  long_description_content_type="text/markdown",
  url="https://github.com/seanghay/khmernormalizer",
  author="Seanghay Yath",
  author_email="seanghay.dev@gmail.com",
  packages=["khmernormalizer"],
  package_dir={"khmernormalizer": "khmernormalizer"}, 
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Natural Language :: English",   
  ],
  install_requires=[
    "regex",
    "emoji==2.6.0",
    "ftfy==6.1.1"
  ],
  package_data={'': ["*"]},
  include_package_data=True,
  python_requires='>=3.7'
)