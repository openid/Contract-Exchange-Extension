import sys
import os
import commands
import re
import libxml2
import random
import sha
import base64

class rsa:

    def __init__(self,cname ):
        self.cname = cname
        self.subject   = "/CN=%s /OU=sys.%s /O=sys /C=JP" % ( self.cname ,self.cname )
        self.x('mkdir -p %s' % (self.cname) )

        self.prikey = self.cname +"/pri.pem"
        self.pubkey = self.cname +"/pub.pem"
        self.csr = self.cname +"/csr.pem"
        self.cert= self.cname + "/cert.pem"
        self.cert_der = self.cname + "/cert.der"
        self.cert_pkcs12 = self.cname + "/cert.pfx"
        self.rand = self.cname = "/rand.txt"
        self.keylen=1024


    def x(self,cmd):
        print "executing....",cmd
        return commands.getoutput(cmd)

    def remove_certs(self):
        self.x('rm -rf %s' % (self.cname) )
        self.x('mkdir %s' % (self.cname) )


    def create_random(self):
        self.x( 'date | openssl dgst  > %s' % (self.rand))

    def create_pri_key(self):
        self.x( 'openssl genrsa -rand %s -passout pass:%s -out %s -des3 %d ' % (
                self.rand , self.cname,self.prikey,self.keylen) )

    def create_csr(self):
        self.x('openssl req -new -key %s -passin pass:%s -out %s -subj "%s" ' % (
                self.prikey , self.cname, self.csr,self.subject ))

    def strip_pri_key_pass(self):
        self.x('openssl rsa -passin pass:%s -in %s  -out %s' % (
            self.cname, self.prikey , self.prikey) )

    def create_cert(self):
        self.x('openssl x509 -in %s  -out %s -req -signkey %s' % (
                self.csr , self.cert , self.prikey ))

    def create_cert_der(self):
        self.x('openssl x509 -in %s -outform DER -out %s ' % (
                self.cert , self.cert_der ))
        
    def create_pub_key(self):
        self.x('openssl x509  -pubkey -in %s > %s' %(
                self.cert , self.pubkey ))

    def create_cert_pkcs12(self):
        self.x('openssl pkcs12 -export -passout pass:%s -inkey %s -in %s  -out %s ' % (
                self.cname, self.prikey, self.cert , self.cert_pkcs12 ))

    @classmethod
    def  generate(cls,cname='hdknr.deb'):
        print "generation certificates for ",cname
        r = rsa(cname)
        r.remove_certs()
        r.create_random()
        r.create_pri_key()
        r.create_csr()
        r.strip_pri_key_pass()
        r.create_cert()
        r.create_cert_der()
        r.create_cert_pkcs12()
        r.create_pub_key()

        return r

if __name__ == '__main__':
    rsa.generate()
