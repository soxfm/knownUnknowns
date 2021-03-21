# ECDSA: The digital signature algorithm of a better internet
---

  The computational cost of the cryptography required on our servers is one of those challenges. Elliptic curve cryptography (ECC) is one of the more promising technologies in this area. ECC-enabled TLS is faster and more scalable on our servers and provides the same or better security than the default cryptography in use on the web.
> the elliptic curve digital signature algorithm (ECDSA), can be used to improve performance on the Internet. 

## Private and Public Keys, Digital Signatures
---

  In public key cryptography each person has a pair of keys: a public key and a private key. These are typically numbers that are chosen to have a specific mathematical relationship. In RSA, the public key is a large number that is a product of two primes, plus a smaller number. The private key is a related number. In ECC, the public key is an equation for an elliptic curve and a point that lies on that curve. The private key is a number. 

**Digital Signatures**

  The private key can be used to create a digital signature for any piece of data using a digital signature algorithm. This typically involves taking a cryptographic hash of the data and operating on it mathematically using the private key. Anyone with the public key can check that this signature was created using the private key and the appropriate signature validation algorithm. A digital signature is a powerful tool because it allows you to publicly vouch for any message.

__ A Website's certificate usually contains two primers:__
- Identity Information: To whom the certificate belongs and to which domains it extends its validity.
	- Public Key: Public half of a key pair: the site owner controls and keeps secret the associated private key.
> The certificate is digitally signed by a trusted certificate authority who validates the identity of the site owner.

###### History
---

Since the introduction of SSL by Netscape in 1994, certificates for web sites have typically used a public/private key pair based on the RSA algorithm. As the SSL specification evolved into TLS, support for different public key algorithms were added. One of the supported algorithms is ECDSA which is based on elliptic curves.

Despite the number of options available in TLS, almost all certificates used on the web today are RSA-based. Web sites have been slow to adopt new algorithms because they want to maintain support for legacy browsers that don’t support the new algorithms. Even as late as 2012, out of 13 million TLS certificates found in a scan of the internet, fewer than 50 use an ECDSA key pair.



### ECDSA in Current, Common, Popular internet Culture: BTC
---

Bitcoin is a good example of a system that relies on ECDSA for security. Every Bitcoin address is a cryptographic hash of an ECDSA public key. The ownership of the account is determined by who controls the ECDSA private key. To transfer an amount of Bitcoin to another person, you create a message that says something along the lines of “I give this Bitcoin to address X”, sign it with your private key and submit it to the Bitcoin system. The linchpin of the security and consistency of the Bitcoin system is the security of ECDSA private keys.

Elliptic curves and ECDSA in particular are also used in messaging and systems security. In Apple’s recent white paper on iOS security, they relayed how they use ECDSA extensively in the Apple ecosystem. Messages through iMessage are signed with ECDSA and iCloud keychain syncing relies on ECDSA. More and more technologies are using ECDSA for security, including end-to-end encrypted messaging services TextSecure and CryptoCat.

### ECDSA vs RSA
---
Why is ECDSA the algorithm of choice for new protocols when RSA is available and has been the gold standard for asymmetric cryptography since 1977? It boils down to the fact that we are better at breaking RSA than we are at breaking ECC.

##### ** Breaking KEYS **
---

- Breaking an RSA key requires you to factor a large number. We are pretty good at factoring large numbers and getting better all the time. Breaking an ECDSA key requires you to solve the Elliptic Curve Discrete Logarithm Problem (ECDLP). The mathematical community has not made any major progress in improving algorithms to solve this problem since is was independently introduced by Koblitz and Miller in 1985.

- This means that with ECDSA you can get the same level of security as RSA but with smaller keys. Smaller keys are better than larger keys for several reasons. Smaller keys have faster algorithms for generating signatures because the math involves smaller numbers. Smaller public keys mean smaller certificates and less data to pass around to establish a TLS connection. This means quicker connections and faster loading times on websites.

> According to the (ECRYPT II)[](http://www.keylength.com/en/3/) recommendations on key length, a 256-bit elliptic curve key provides as much protection as a 3,248-bit asymmetric key. Typical RSA keys in website certificates are 2048-bits. If we compare the portion of the TLS handshake that happens on the server for 256-bit ECDSA keys against the cryptographically much weaker 2048-bit RSA key.

__ NOTE: The Master's Guide to Classic Cryptography: (The Handbook of Applied Cryptography)[](http://cacr.uwaterloo.ca/hac/)
