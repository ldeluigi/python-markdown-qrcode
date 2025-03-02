
#!/usr/bin/env python
 
"""
QRcode markdown filter
========================
 
- Copyright (c) 2011 Zenobius Jiricek
    - Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
 
## Format
 
[{ Second encoded data }]
 
"""
 
 
import markdown
from io import BytesIO
from .QrCodeLib import *
from base64 import b64encode
 
class QrCodeExtension(markdown.extensions.Extension):
  """ QRcode Extension for Python-Markdown. """
  def __init__(self, configs={}):
    # Set extension defaults
    self.config = {
      "pixelsize"  : [  4, "Pixel Size of each dark and light bit" ],
      "lightcolor" : [ '#ffffff', "Light Color" ],
      "darkcolor" : [ '#000000', "Dark Color" ],
      "bordercolor" : [ '#000000', "Border Color" ],
      "priority": [ 45, "Priority"]
    }
    # Override defaults with user settings
    for key, value in configs.items():
      self.setConfig(key, value)
 
  def add_inline(self, md, name, pattern_class, pattern):
    objPattern = pattern_class(pattern, self.config)
    objPattern.md = md
    objPattern.ext = self
    md.inlinePatterns.register(objPattern, name, self.getConfig('priority'))
 
  def extendMarkdown(self, md, md_globals):
    self.add_inline(md, 'qrcode', BasicQrCodePattern, r'\[\{\s(?P<data>.*?)\s\}\]')

class BasicQrCodePattern(markdown.inlinepatterns.Pattern):
  def __init__(self, pattern, config):
    self.pattern = pattern
    self.config = config
    markdown.inlinepatterns.Pattern.__init__(self, pattern)
	
  def handleMatch(self, match):
 
    if match :
      pixel_size = self.config['pixelsize'][0]
      light_color = self.config['lightcolor'][0]
      dark_color = self.config['darkcolor'][0]
      border_color = self.config['bordercolor'][0]
      qrcodeSourceData = match.group('data')
 
      qrCodeObject = QRCode(pixel_size, QRErrorCorrectLevel.L)
      qrCodeObject.addData( qrcodeSourceData )
      qrCodeObject.make()
      qrCodeImage = qrCodeObject.makeImage(
        pixel_size = pixel_size,
		border_color = border_color,
        dark_colour = dark_color,
		light_colour = light_color
      )
      qrCodeImage_File = BytesIO()
      qrCodeImage.save(qrCodeImage_File , format= 'PNG')
      etree = markdown.util.etree
      container = etree.Element('div')
      element = etree.SubElement(container, 'img')
      element.set('class','qrcode')
      element.set('src', 'data:image/png;base64,%s' % str(b64encode( qrCodeImage_File.getvalue() ),'utf-8') )
      qrCodeImage_File.close()
 
      return element
 
    else :
      return None
 
def makeExtension(*args, **kwargs):
  return QrCodeExtension(kwargs)
