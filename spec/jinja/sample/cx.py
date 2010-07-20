import simplejson
import sys
import base64
import uuid
import cStringIO
from binascii import unhexlify,hexlify
from datetime import datetime
#
from M2Crypto import RSA, BIO, Rand, m2, EVP, X509
from certs import rsa
#
class CX:
    CXNS=r'http://specs.openid.net/extensions/cx/1.0/#(.+)'

    def __init__(self,jtype=''):
        self.jtype = jtype
        self.json = simplejson.loads('{}') 

    @classmethod
    def load_cert(cls,party):
        r = rsa(party)
#        print r.cert ,'is certificate PEM.'
        return X509.load_cert(r.cert )       #X509.X509

    @classmethod
    def load_publickey(cls,party='',x509=None):
        if x509 == None:
            x509 = cls.load_cert(party)
        r = x509.get_pubkey().get_rsa()
        ret = RSA.RSA_pub( r.rsa )
        ret.container= r
        return ret 

    @classmethod
    def load_privatekey(cls,party):
        r = rsa(party)
        return RSA.load_key(r.prikey )

    @classmethod
    def public_encrypt(cls,data,pubkey=None,party =''):
        ''' default : PKCS#1 padding
        ''' 
        if pubkey == None:
            pubkey = cls.load_publickey(party)
        return pubkey.public_encrypt(data,RSA.pkcs1_padding)
        
    @classmethod
    def private_decrypt(cls,prikey,data):
        return prikey.private_decrypt(data,RSA.pkcs1_padding)

    @classmethod
    def generate_sharedkey(cls):
        ''' ToDo: think better later.
        '''
        return unhexlify( uuid.uuid1().hex )

    @classmethod
    def generate_iv(cls):
        ''' ToDo: think better later.
        '''
        return unhexlify( uuid.uuid1().hex )
                

    def canonicalize(self):
        return base64.urlsafe_b64encode(simplejson.dumps(self.json))

 
    def encrypt_aes_cbc_128(self,key,iv):
        ''' ToDo : NOT YET
         
        '''
        return ""

    def jsonenc(self,party):
        ''' JSON Encryption Envelope

            enc_type_asy : (default) "http://www.w3.org/2001/04/xmlenc#rsa-1_5"
            enc_type     : (default) "AES-128-CBC"
                         : OpenSSL's block size 128 bit. IV and Key should be 128 bit.
            enc_ref      : (option ) ...URI to PEM formatted X.509 certificate
            enc_pem      : (option ) ...PEM of X.509 certificate (BASE64URL)
            enc_thumbprint:(option ) .... A SHA1 of the DER encoded certificate.
        '''
        new_cx = CX()

        key = CX.generate_sharedkey()
        iv  = CX.generate_iv() 

        new_cx.json['object_type'] = "http://jsonenc.info/json-encryption/"
        new_cx.json['data_type'] = "application/json"
        new_cx.json['data'] =  base64.safe_b64encode( self.encrypt_aes_cbc_128(key,iv) )  
        new_cx.json['enc_key'] = base64.safe_b64encode( CX.public_encrypt(key,party=party)
        new_cx.json['enc_iv'] = base64.safe_b64encode(iv)
        
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


#    @cxtest
    def testCertEncrypt(self):

        pub = CX.load_publickey( CXTest.PARTIES[0])
        pri = CX.load_privatekey( CXTest.PARTIES[0])

        for c in range(3):
            src = str(datetime.now())
            enc=CX.public_encrypt(pub,src )
            dec =CX.private_decrypt(pri,enc)
            print (src == dec ),src,dec

        return True

    def testCert(self):
        r=rsa(CXTest.PARTIES[0])
        print r.cert
        x=X509.load_cert(r.cert )       #X509.X509
        pub = x.get_pubkey().get_rsa()  #RSA.RSA
        rsa_pub = RSA.RSA_pub(pub.rsa)  #RSA.RSA_pub
        print rsa_pub.public_encrypt('data', RSA.pkcs1_padding)
        return True


    def cipher_filter(self, cipher, inf, outf):
        while 1:
            buf=inf.read()
            if not buf:
                break
            outf.write(cipher.update(buf))
        outf.write(cipher.final())
        return outf.getvalue()

    def testAes(self):
        enc = 1
        dec = 0
        tests = [
            # test vectors from rfc 3602
            #Case #1: Encrypting 16 bytes (1 block) using AES-CBC with 128-bit key
            {
            ' KEY': '06a9214036b8a15b512e03d534120006',
            'IV':  '3dafba429d9eb430b422da802c9fac41',
            'PT':  'Single block msg',
            'CT':  'e353779c1079aeb82708942dbe77181a',
            },
            
            #Case #2: Encrypting 32 bytes (2 blocks) using AES-CBC with 128-bit key
            {
            'KEY': 'c286696d887c9aa0611bbb3e2025a45a',
            'IV':  '562e17996d093d28ddb3ba695a2e6f58',
            'PT':  unhexlify('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'),
            'CT':  'd296cd94c2cccf8a3a863028b5e1dc0a7586602d253cfff91b8266bea6d61ab1',
            },
            
            #Case #3: Encrypting 48 bytes (3 blocks) using AES-CBC with 128-bit key
            {
            'KEY': '6c3ea0477630ce21a2ce334aa746c2cd',
            'IV':  'c782dc4c098c66cbd9cd27d825682c81',
            'PT':  'This is a 48-byte message (exactly 3 AES blocks)',
            'CT':  'd0a02b3836451753d493665d33f0e8862dea54cdb293abc7506939276772f8d5021c19216bad525c8579695d83ba2684',
            },
        ]
       
        # Test with padding
        for test in tests:
            # encrypt (op=enc [1])
            k=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=enc)
            pbuf=cStringIO.StringIO(test['PT'])
            cbuf=cStringIO.StringIO()
            ciphertext = hexlify(self.cipher_filter(k, pbuf, cbuf))
            cipherpadding = ciphertext[len(test['PT']) * 2:]

            print ciphertext
            ciphertext = ciphertext[:len(test['PT']) * 2] # Remove the padding from the end
            print ciphertext,cipherpadding
            pbuf.close()
            cbuf.close()
            self.assertEqual(ciphertext, test['CT'])

            # decrypt (op=dec [0])
            j=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=dec)
            pbuf=cStringIO.StringIO()
            cbuf=cStringIO.StringIO(unhexlify(test['CT'] + cipherpadding))
            plaintext=self.cipher_filter(j, cbuf, pbuf)
            print plaintext
            pbuf.close()
            cbuf.close()
            self.assertEqual(plaintext, test['PT'])
            print "**"

if __name__ == '__main__':
#    CXTest.prepare_keys()  
    unittest.main() 
