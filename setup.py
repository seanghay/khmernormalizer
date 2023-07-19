import setuptools
import khmernormalizer

with open("readme.md") as f:
  readme_md = f.read()
    
setuptools.setup(
  name="khmernormalizer",
  version=khmernormalizer.__version__,
  description="A missing toolkit for Khmer Natural Language Processing.",
  long_description=readme_md,
  long_description_content_type="text/markdown",
  packages=["khmernormalizer"],
  classifiers=[],
  install_requires=[
    "regex",
    "emoji==2.6.0",
    "ftfy==6.1.1"
  ],
  package_data={'': ["*"]},
  python_requires='>=3.5'
)