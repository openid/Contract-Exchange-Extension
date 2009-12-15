import sys
from StringIO import StringIO
from lxml import etree
#
if __name__ == '__main__':
    (doc,xsd) = [ etree.parse( StringIO( open(f).read())) for f in  sys.argv[1:] ]
    print etree.XMLSchema(xsd).validate(doc) 
    print etree.XMLSchema(xsd).assertValid(doc)
