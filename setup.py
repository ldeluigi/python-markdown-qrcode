from distutils.core import setup
setup(
  name='markdown_qrcode',
  version='0.0.4',
  maintainer="none",
  # maintainer_email="lucadelu97@gmail.com",
  url="github.com/ldeluigi/python-markdown-qrcode",
  py_modules=[
    'pymdownmx.qrcode',
    'pymdownmx.extension',
    'pymdownmx.QrCodeLib',
  ],
  license='LICENSE.md',
  description='A markdown extension to insert qrcode datauri images based on supplied data.',
  long_description=open('README.md').read(),
)

