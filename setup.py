from setuptools import setup, find_packages

setup(
  name='markdown_qrcode',
  packages = find_packages(),
  version='0.0.4',
  author="Many",
  author_email="lucadelu97@gmail.com",
  url="github.com/ldeluigi/python-markdown-qrcode",
  license='LICENSE.md',
  description='A markdown extension to insert qrcode datauri images based on supplied data.',
  long_description=open('README.md').read(),
)

