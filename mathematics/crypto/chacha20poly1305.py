# base implementation based upon (tlslite-ng)[https://github.com/tomato42/tlslite-ng]
# macOS cryptography api extendable framework implementation

import os
from chacha20poly1305 import ChaCha20Poly1305

key = os.urandom(32)
cip = ChaCha20Poly1305(key)

nonce = os.urandom(12)
ciphertext = cip.encrypt(nonce, b'test')

plaintext = cip.decrypt(nonce, ciphertext)
print(plaintext)

##
#    pip3 install chacha20poly1305
##
