from M2Crypto import BIO, SMIME, X509, Rand
#
cert=".certs/book.com/cert.pem"
rand=".certs/book.com/rand.pem"
json='{ "name":"hdknr","address":"shibuya" }'

# Buffer
buf = BIO.MemoryBuffer(json)

# Seed the PRNG
Rand.load_file(rand,-1)

# S/MIME object
s = SMIME.SMIME()

# Load certificate
x509 = X509.load_cert(cert)
sk=X509.X509_Stack()
sk.push(x509)
s.set_x509_stack(sk)

#Set cipher: 3-key triple-DES in CBC mode.
s.set_cipher(SMIME.Cipher('des_ede3_cbc'))

# Encrypt the buffer.
p7 = s.encrypt(buf)
#p7  = s.sign(buf)

out = BIO.MemoryBuffer()
s.write(out, p7)
smime = out.read() 
print smime
headers, body = smime.split('\n\n', 1)

#
Rand.save_file(rand)

