import simplejson
import sys

#class CX:
#    CXNS=r'http://specs.openid.net/extensions/cx/1.0/#(.+)'
#
#    def __init__(self,jtype):
#        self.jtype = jtype
#        self.json = simplejson.loads('{}') 
#
#    @classmethod
#    def parse_jtype(cls,jobj):
#        if jobj.has_key('type'):
#            pass
#            
#    @classmethod
#    def parse(cls,json_string ):
#        j = simplejson.loads(json_string)
#
#class Request:
#    def __init__(self):
#        pass 


import traceback
def cxtest(fn):
    def deco_cxtest(*args):
        stack = traceback.extract_stack()
        scriptName, lineNum, funcName, lineOfCode = stack[-2]
        msg = "**** %s is calling %s.%s" % (funcName,args[0].__class__.__name__ ,fn.func_name )
        print 
        print '*' * len(msg)
        print msg
        print '*' * len(msg)

        return fn(*args)
    return deco_cxtest

import unittest
from certs import rsa
from M2Crypto import RSA, BIO, Rand, m2, EVP, X509

class CXTest( unittest.TestCase ):
    PARTIES=['book.com','ship.com','pay.com','op.net']

    @classmethod
    def prepare_keys(cls):
        ''' prepare all keys and certificates 
        '''
        for p in cls.PARTIES:
            rsa.generate(p)

    def setUp(self):
        print "setup"

    def tearDown(self):
        print "teardown"


    def testCertEncryptSample(self):
        ''' based on M2Crypt sample
        '''
        r=rsa(CXTest.PARTIES[0])
        print r.cert
        x=X509.load_cert(r.cert )       #X509.X509
        pub = x.get_pubkey().get_rsa()  #RSA.RSA
        print pub.public_encrypt('data',RSA.pkcs1_padding)
        return True

#    @cxtest
    def testCertEncrypt(self):
        r=rsa(CXTest.PARTIES[0])
        print r.cert
        x=X509.load_cert(r.cert )       #X509.X509
        pub = x.get_pubkey().get_rsa()  #RSA.RSA
        rsa_pub = RSA.RSA_pub(pub.rsa)  #RSA.RSA_pub
        print pub,rsa_pub
        print rsa_pub.public_encrypt('data', RSA.pkcs1_padding)
        return True

#    @cxtest
    def testPublicEncrypt(self):
        r=rsa(CXTest.PARTIES[0])
#        k=RSA.load_pub_key('x.pem') #r.pubkey)
        k=RSA.load_pub_key(r.pubkey)
        print k,dir(k)
        e= k.public_encrypt('data', RSA.pkcs1_padding)
        print e
 
        return True 

#    @cxtest
    def testTwo(self):
        return True 

if __name__ == '__main__':
#    CXTest.prepare_keys()  
    unittest.main() 
