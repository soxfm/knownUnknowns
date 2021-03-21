# HTTPS (TLS Encryption)
---

The TLS cipher suite consists of one algorithm for each of the following:
 - Key establishment(typically Difie-Hellman variant or RSA)
- Authentication (the certificate type)
- Confidentiality (a symmetric cipher
- integrity (a hash function)

### Block Ciphers & Stream Ciphers
---

- In a **Block Cipher**: the data is broken up into chunks of a fixed size and each block is encrypted.
- In a **Stream Cipher**: the data is encrypted one byte at a time. 
> Block ciphers are generally fast in hardware and somewhat slower in software; while stream ciphers often provide faster software implementations.

### TLS Block Cipher
---

> TLS has a secure block cipher, AES, that has been implemented in hardware and is generally very fast. One current problem with TLS is that there is no secure choice of stream cipher. The de facto stream cipher for TLS is RC4, which has been shown to have biases and is no longer considered secure.

AES is a fine cipher to use on most modern computers. Intel processors since Westmere in 2010 come with AES hardware support that makes AES operations effectively free.

This makes it an ideal cipher choice for moderns dekstop web browsers. However, the ubiquity of ever-emerging internet connected devices; such as phones and tablets; - don’t typically have cryptographic hardware for AES and are therefore required to use software implementations of ciphers.

IETF Internet Draft:
ChaCha20 and Poly1305 for IETF protocols []
The ChaCha20 cipher is designed to provide 256-bit security.

The Poly1305 authenticator is designed to ensure that forged messages are rejected with a probability of 1-(n/(2^102)) for a 16n-byte message, even after sending 2^64 legitimate messages, so it is SUF-CMA in the terminology of [AE](http://cseweb.ucsd.edu/~mihir/papers/oem.html).

__note: there is a revised 2015 draft namely: ("ChaCha20 and Poly1305 for IETF protocols: draft-irtf-cfrg-chacha20-poly1305-10") []__


### Poly 1305 Authentication
---

  Poly1305 provides authentication, protecting TLS against attackers inserting fake messages into a secure stream. Poly1305’s key strength is considered strong enough to stop this attack, providing around 100 bits of security. Authentication in TLS is slightly less important than encryption because even if an attacker can add a fake message to the stream, they can’t read the information inside without breaking the encryption key.

> ChaCha20-Poly1305 also uses the current recommended construction for combining encryption and authentication. It’s built using an Authenticated Encryption with Associated Data (AEAD) construction. AEAD is a way of combining a cipher and an authenticator together to get the combined properties of encryption and authentication. This would be done previously with two different algorithms, typically a block cipher and an HMAC
> Authenticated encryption makes it impossible to decrypt a ciphertext out of order which helps rule out a whole class of problems including BEAST, Lucky 13 and POODLE.
