QRCODE Markdown Extension
=========================

Note: Ported to Python 3

## Installation
`pip install git+git://github.com/ldeluigi/python-markdown-qrcode#egg=markdown_qrcode`

## Format

    [{ QR CODE DATA }]

## Config Options

`pixelsize`
: Pixel Size of each dark and light bit. _Default is 4_

`lightcolor`
: The color to use for background bits. _Default is #FFFFFF (white)_

`darkcolor`
: The color to use for foreground bits. _Default is #000000 (black)_

`bordercolor`
: The color to use for each bit borders. _Default is #000000 (black)_

`priority`
: Priority for this plugin

## Extending Python Markdown:
The extension name is 'mdqrcode'

## Format

### Syntax

This is the short syntax:

    [{ str data to encode }]

## Legal

### extension.py

+ Copyright (c) 2011 Zenobius Jiricek
+ Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php


### QrCodeLib.py

Ported from Javascript to Python by Sam Curren

Original Project :
+ Copyright (c) 2009 Kazuhiko Arase
+ http://d-project.googlecode.com/svn/trunk/misc/qrcode/js/qrcode.js
+ Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

### Trademarks

The word "QR Code" is registered trademark of DENSO WAVE INCORPORATED

+ http://www.denso-wave.com/qrcode/faqpatent-e.html

