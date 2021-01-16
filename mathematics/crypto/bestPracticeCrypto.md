# Cryptographic Best Practices

Putting cryptographic primitives together is a lot like putting a jigsaw
puzzle together, where all the pieces are cut exactly the same way, but there
is only one correct solution. Thankfully, there are some projects out there
that are working hard to make sure developers are getting it right.

The following advice comes from years of research from leading security
researchers, developers, and cryptographers. This Gist was [forked from Thomas
Ptacek's Gist][1] to be more readable. Additions have been added from
[Latacora's Cryptographic Right Answers][2].

[1]: https://gist.github.com/tqbf/be58d2d39690c3b366ad
[2]: http://latacora.singles/2018/04/03/cryptographic-right-answers.html

Some others have been added from years of discussions on Twitter, IRC, and
mailing lists that would be too difficult to pin down, or exhaustively list
here.

If at any point, I disagree with some of the advice, I will note it and provide
reasoning why. If you have any questions, or disagreements, [let me know][3].

[3]: https://twitter.com/AaronToponce

### TL;DR

If you take only one thing away from this post, it should be to use a library
that puts these puzzle pieces together correctly for you. Pick one of for your
project:

1. [NaCl][4] - By cryptographer Daniel Bernstein
2. [libsodium][5] - NaCl fork by developer Frank Denis
3. [monocypher][6]- libsodium fork by developer Loup Vaillant 

[4]: https://nacl.cr.yp.to/
[5]: https://download.libsodium.org/doc/
[6]: https://monocypher.org/

Throughout this document, when I refer to "just use NaCl", I mean one of these
libraries.

### Symmetric Encryption

If you are in a position to use a [key management system (KMS)][7], then you
should use KMS. If you are not in a position to use KMS, then you should use
[authenticated encryption with associated data (AEAD)][8].

[7]: https://en.wikipedia.org/wiki/Key_management#Key_management_system
[8]: https://en.wikipedia.org/wiki/Authenticated_encryption

Currently, [the CAESAR competition][9] is being held to find an AEAD algorithm
that doesn't have some of the sharp edges of AES-GCM while also improving
performance. When the announcement of the final portfolio drops, this document
will be updated.

[9]: https://competitions.cr.yp.to/caesar.html

Some notes on AEAD:

* ChaCha20-Poly1305 is faster in software than AES-GCM.
* AES-GCM will be faster than ChaCha20-Poly1305 with AES-NI.
* AES-CTR with HMAC will be faster in software than AES-GCM.
* Poly1305 is also easier than GCM for library designers to implement safely.
* AES-GCM is the industry standard.

The NaCl libraries will handle AEAD for you natively.

**Use, in order of preference:**

1. KMS, if available.
2. The NaCL, libsodium, or monocypher default
3. Chacha20-Poly1305
4. AES-GCM
5. AES-CTR with HMAC

**Avoid:**

1. AES-CBC, AES-CTR by itself
2. [Block ciphers with 64-bit blocks][10], such as Blowfish.
3. OFB mode
4. RC4, which is comically broken

[10]: https://sweet32.info/

### Symmetric Key Length

See my blog post about [The Physics of Brute Force][11] to understand why
256-bit keys is more than sufficient. But rememeber: your AES key is far less
likely to be broken than your public key pair, so the latter key size should be
larger if you're going to obsess about this.

[11]: https://pthree.org/2016/06/19/the-physics-of-brute-force/

If your symmetric key is based on user input, such as a passphrase, then it
should provide at least as many bits of theoretical entropic security as the
symmetric key length. In other words, if your AES key is 128-bits, and is built
from a password, then that passwourd should provide at least 128-bits of
entropy.

As with asymmetric encryption, symmetric encryption key length is a vital
security parameter. Academic, private, and government organizations provide
different recommendations with mathematical formulas to approimate the minimum
key size requirement for security. See [BlueKcrypt's Cryptographyc Key Length
Recommendation][12] for other recommendations and dates.

[12]: https://keylength.com/

To protect data up through 2050, it is recommended to meet the minimum
requirements for symmetric key lengths:

* [Lenstra/Verheul][13]- 109 bits
* [Lenstra Updated][14]- 102 bits
* [ECRYPT II][15]- 256 bits
* [NIST][16]- 192 bits
* [ANSSI][17]- 128 bits
* [IAD-NSA][18]- 256 bits
* [BSI][19]- 128 bits

[13]: http://infoscience.epfl.ch/record/164526/files/NPDF-22.pdf
[14]: http://infoscience.epfl.ch/record/164539/files/NPDF-32.pdf
[15]: http://www.ecrypt.eu.org/ecrypt2/documents/D.SPA.20.pdf
[16]: http://csrc.nist.gov/groups/ST/toolkit/key_management.html
[17]: http://www.ssi.gouv.fr/uploads/2015/01/RGS_v-2-0_B1.pdf
[18]: https://www.iad.gov/iad/library/ia-guidance/ia-solutions-for-classified/algorithm-guidance/commercial-national-security-algorithm-suite-factsheet.cfm
[19]: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile

See also the NSA [Fact Sheet Suite B Cryptography][20] and [RFC 3766][21] for
additional recommendations and math algorithms for calculating strengths based
on calendar year.

[20]: https://www.nsa.gov/ia/programs/suiteb_cryptography/index.shtml
[21]: https://tools.ietf.org/html/rfc3766

Personally, I don't see any problem with using 256-bit key lengths. So, my
recommendation would be:

**Use:**

1. Minimum- 128-bit keys
2. Maximum- 256-bit keys

**Avoid:**

1. Constructions with huge keys
2. Cipher "cascades"
3. Key sizes under 128 bits

### Symmetric Signatures

If you're authenticating but not encrypting, as with API requests, don't do
anything complicated. There is a class of crypto implementation bugs that arises
from how you feed data to your MAC, so, if you're designing a new system from
scratch, Google "crypto canonicalization bugs". Also, use a secure compare
function. 

If you use HMAC, people will feel the need to point out that SHA-3 (and the
truncated SHA-2 hashes) can do “KMAC”, which is to say you can just concatenate
the key and data, and hash them to be secure. This means that in theory, HMAC
is doing unnecessary extra work with SHA-3 or truncated SHA-2. But who cares?
Think of HMAC as cheap insurance for your design, in case someone switches to
non-truncated SHA-2.

**Use:**

1. HMAC-SHA-512/256
2. HMAC-SHA-512/224
3. HMAC-SHA-384
4. HMAC-SHA-224
5. HMAC-SHA-512
6. HMAC-SHA-256

**Alternately, use in order of preference:**

1. Keyed BLAKE2b
2. Keyed BLAKE2s
3. Keyed SHA3-512
4. Keyed SHA3-256

**Avoid:**

1. HMAC-MD5
2. HMAC-SHA1
3. Custom "keyed hash" constructions
4. Complex polynomial MACs
5. Encrypted hashes
6. Anything CRC

### Hashing

If you can get away with it you want to use hashing algorithms that truncate
their output and sidesteps length extension attacks. Meanwhile: it's less likely
that you'll upgrade from SHA-2 to SHA-3 than it is that you'll upgrade from
SHA-2 to BLAKE2, which is faster than SHA-3, and SHA-2 looks great right now, so
get comfortable and cuddly with SHA-2.

**Use (pick one):**

1. SHA-2 (fast, time-tested, industry standard)
2. BLAKE2 (fastest, SHA-3 finalist)
3. SHA-3 (slowest, industry standard)

**Avoid:**

1. SHA-1
2. MD5
3. MD6
4. EDON-R (I'm looking at you OpenZFS)

### Random Numbers

When creating random IDs, numbers, URLs, initialization vectors, or anything
that is *random*, then you should [always use your operating system's
kernelspace CSPRNG][31] On GNU/Linux (including Android), BSD, or Mac (including
iOS), this is `/dev/urandom`. On Windows, this is [CryptGenRandom][32].

**NOTE:** [/dev/random is **_not_** more secure then /dev/urandom][33]. They
use the same CSPRNG. They only time you would obsess over this, is when working
on an information theoretic cryptographic primitive that exploits the blocking
aspects of `/dev/random`, which you aren't doing (you would know it when you're
doing it).

The only time you should ever use a userspace RNG, is when you're in a
constrained environment, such as embedded firmware, where the OS RNG is not
available. In that case, use [fast-key erasure][34]. The problem here, however,
is making sure that it is properly seeded with entropy on each boot. This is
harder than it sounds, so really, at all costs, this should only be used as a
worst-scenario fallback.

[31]: http://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/
[32]: https://msdn.microsoft.com/en-us/library/windows/desktop/aa379942(v=vs.85).aspx
[33]: https://security.stackexchange.com/a/3939
[34]: https://blog.cr.yp.to/20170723-random.html

**Use:**

1. Your operating system's CSPRNG.
2. Fast key erasure (as a fallback).

**Create:** 256-bit random numbers

**Avoid:**

1. Userspace random number generators
2. `/dev/random`

### Password Hashing

When using scrypt for password hashing, be aware that it is very [sensitive to
the parameters][35], making it possible to end up weaker than bcrypt, and
suffers from time-memory trade-off ([source #1][36] and [source #2][37]). When
using bcrypt, make sure to use the following algorithm to prevent [the leading
NULL byte problem][38]. and the 72-character password limit:

    bcrypt(base64(sha-512(password)))

[35]: http://blog.ircmaxell.com/2014/03/why-i-dont-recommend-scrypt.html
[36]: http://www.openwall.com/lists/crypt-dev/2013/03/21/1
[37]: http://www.openwall.com/lists/crypt-dev/2013/03/17/1
[38]: http://blog.ircmaxell.com/2015/03/security-issue-combining-bcrypt-with.html

Initially, I was hesitant to recommend Argon2 for general production use. I no
longer feel that way. It was the winner of the [Password Hashing
Competition][39], has had ample analysis, even before the competition finished,
and is showing no signs of serious weaknesses.

[39]: https://password-hashing.net/

Each password hashing algorithm requires a "cost" to implement correctly. For
Argon2, this is using a sufficient time on the CPU and a sufficient amount of
RAM. For scrypt, this is using at least 16 MB of RAM. For bcrypt, this is a
cost of at least "5". For sha512crypt and sha256crypt, this it at least 5,000
rounds. For PBKDF2, this is at least 1,000 rounds.

Jeremi Gonsey, a professional password cracker, publishes benchmarks with
Nvidia GPU clusters, such as with [8x Nvidia GTX 1080 Ti GPUs][40]. It's worth
looking over those numbers.

[40]: https://gist.github.com/epixoip/ace60d09981be09544fdd35005051505

**Use, in order of preference:**

1. Argon2 (tune appropriately)
2. scrypt (>= 16 MB)
3. bcrypt (>= 5)
4. sha512crypt (>= 5,000 rounds)
5. sha256crypt (>= 5,000 rounds)
6. PBKDF2 (>= 1,000 rounds)

**Avoid:**

1. Plaintext
2. Naked SHA-2, SHA-1, MD5
3. Complex homebrew algorithms
4. Any encryption algorithm

### Asymmetric Encryption

It's time to stop using anything RSA, and start using NaCL. Of all the
cryptographic "best practices", this is the one you're least likely to get
right on your own. NaCL has been designed to prevent you from making stupid
mistakes, it's highly favored among the cryptographic community, and focuses on
modern, highly secure cryptographic primitives.

It's time to start using ECC. Here are several reasons you should stop using
RSA and switch to elliptic curve software:

* Progress in attacking RSA --- really, all the classic multiplicative group
  primitives, including DH and DSA and presumably ElGamal --- is proceeding
  faster than progress against elliptic curves.
* RSA (and DH) drag you towards "backwards compatibility" (ie: downgrade-attack
  compatibility) with insecure systems. Elliptic curve schemes generally don't
  need to be vigilant about accidentally accepting 768-bit parameters.
* RSA begs implementors to encrypt directly with its public key primitive,
  which is usually not what you want to do: not only does accidentally
  designing with RSA encryption usually forfeit forward-secrecy, but it also
  exposes you to new classes of implementation bugs. Elliptic curve systems
  don't promote this particular foot-gun. 
* The weight of correctness/safety in elliptic curve systems falls primarily on
  cryptographers, who must provide a set of curve parameters optimized for
  security at a particular performance level; once that happens, there aren't
  many knobs for implementors to turn that can subvert security. The opposite
  is true in RSA. Even if you use RSA-KEM or RSA-OAEP, there are additional
  parameters to supply and things you have to know to get right.

If you absolutely have to use RSA, do use RSA-KEM. But don't use RSA. Use ECC.

**Use:** NaCL, libsodium, or monocypher

**Avoid:**

1. Really, anything RSA
2. ElGamal
3. OpenPGP, OpenSSL, BouncyCastle, etc.

### Asymmetric Key Length

As with symmetric encryption, asymmetric encryption key length is a vital
security parameter. Academic, private, and government organizations provide
different recommendations with mathematical formulas to approimate the minimum
key size requirement for security. See [BlueKcrypt's Cryptographyc Key Length
Recommendation][41] for other recommendations and dates.

[41]: https://keylength.com

To protect data up through 2050, it is recommended to meet the minimum
requirements for asymmetric key lengths:

Method | RSA | ECC | D-H Key | D-H Group
------ | --- | --- | ------- | ---------
[Lenstra/Verheul][42] | 4047 | 206 | 193 | 4047 
[Lenstra Updated][43] | 2440 | 203 | 203 | 2440
[ECRYPT II][44] | 15424 | 512 | 512 | 15424
[NIST][45] | 7680 | 384 | 384 | 7680
[ANSSI][46] | 3072 | 256 | 200 | 3072
[BSI][47] | 3000 | 250 | 250 | 3000

[42]: http://infoscience.epfl.ch/record/164526/files/NPDF-22.pdf
[43]: http://infoscience.epfl.ch/record/164539/files/NPDF-32.pdf
[44]: http://www.ecrypt.eu.org/ecrypt2/documents/D.SPA.20.pdf
[45]: http://csrc.nist.gov/groups/ST/toolkit/key_management.html
[46]: http://www.ssi.gouv.fr/uploads/2015/01/RGS_v-2-0_B1.pdf
[47]: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile

See also the NSA [Fact Sheet Suite B Cryptography][48] and [RFC 3766][49] for
additional recommendations and math algorithms for calculating strengths based
on calendar year.

[48]: https://www.nsa.gov/ia/programs/suiteb_cryptography/index.shtml
[49]: https://tools.ietf.org/html/rfc3766

Personally, I don't see any problem with using 2048-bit RSA/DH group and 256-bit
ECC/DH key lengths. So, my recommendation would be:

**Use:**

1. 256-bit minimum for ECC/DH Keys
2. 2048-bit minimum for RSA/DH Group (but you're not using RSA, right?)

**Avoid:** Not following the above recommendations.

### Asymmetric Signatures

The two dominating use cases within the last 10 years for asymmetric signatures
are cryptocurrencies and forward-secret key agreement, as with ECDHE-TLS. The
dominating algorithms for these use cases are all elliptic-curve based. Be wary
of new systems that use RSA signatures.

In the last few years there has been a major shift away from conventional DSA
signatures and towards misuse-resistent "deterministic" signature schemes, of
which EdDSA and RFC6979 are the best examples. You can think of these schemes
as "user-proofed" responses to the Playstation 3 ECDSA flaw, in which reuse of
a random number leaked secret keys. Use deterministic signatures in preference
to any other signature scheme. 

Ed25519, the NaCl default, is by far the most popular public key signature
scheme outside of Bitcoin. It’s misuse-resistant and carefully designed in
other ways as well. You shouldn’t freelance this either; get it from NaCl.

**Use, in order of preference:**

1. NaCL, libsodium, or monocypher
2. Ed25519
3. RFC6979 (deterministic DSA/ECDSA)

**Avoid:**

1. Anything RSA
4. ECDSA
5. DSA

### Diffie-Hellman

Developers should not freelance their own encrypted transports. To get a sense
of the complexity of this issue, read the documentation for the [Noise Protocol
Framework][50]. If you're doing a key-exchange with Diffie-Hellman, you
probably want an authenticated key exchange (AKE) that resists key compromise
impersonation (KCI), and so the primitive you use for Diffie-Hellman is not the
only important security concern.

[50]: http://noiseprotocol.org/

It remains the case: if you can just use NaCl, use NaCl. You don’t even have to
care what NaCl does. That’s the point of NaCl.

Otherwise: use Curve25519. There are libraries for virtually every language. In
2015, we were worried about encouraging people to write their own Curve25519
libraries, with visions of Javascript bignum implementations dancing in our
heads. But really, part of the point of Curve25519 is that the entire curve was
carefully chosen to minimize implementation errors. Don’t write your own! But
really, just use Curve25519.

[Don’t do ECDH with the NIST curves][51], where you’ll have to carefully verify
elliptic curve points before computing with them to avoid leaking secrets. That
attack is very simple to implement, easier than a CBC padding oracle, and far
more devastating.

[51]: https://safecurves.cr.yp.to/

The previos edition of this document included a clause about using DH-1024 in
preference to sketchy curve libraries. You know what? That’s still a valid
point. Valid and stupid. The way to solve the “DH-1024 vs. sketchy curve
library” problem is, the same as the “should I use Blowfish or IDEA?” problem.
Don’t have that problem. Use Curve25519.

**Use, in order of preference:**

1. NaCL, libsodium, or monocypher
2. Curve25519
3. 2048-bit Diffie-Hellman Group #14

**Avoid:**

1. Conventional DH
2. SRP
3. J-PAKE
4. Handshakes and negotiation
5. Elaborate key negotiation schemes that only use block ciphers
6. srand(time())

### Website security

By "website security", we mean "the library you use to make your web server
speak HTTPS". If you can pay a web hosting provider to worry about this
problem for you, then you do that. Otherwise, use OpenSSL.

There was a dark period between 2010 and 2016 where OpenSSL might not have been
the right answer, but that time has passed. OpenSSL has gotten better, and,
more importantly, OpenSSL is on-the-ball with vulnerability disclosure and
response.

Using anything besides OpenSSL will drastically complicate your system for
little, no, or even negative security benefit. This means avoid [LibreSSL][52],
[BoringSSL][53], or [BearSSL][54] for the time being. Not because they're bad,
but because OpenSSL really is the Right Answer here. Just keep it simple; use
OpenSSL.

[52]: https://www.libressl.org/
[53]: https://boringssl.googlesource.com/boringssl/
[54]: https://bearssl.org/

Speaking of simple: [LetsEncrypt][55] is free and automated. Set up a cron job
to re-fetch certificates regularly, and test it.

[55]: https://letsencrypt.org/

**Use:**

1. A web hosting provider, like AWS.
2. OpenSSL with Let's Encrypt

**Avoid:**

1. PolarSSL
2. GnuTLS
3. MatrixSSL
4. LibreSSL
5. BoringSSL
6. BearSSL

### Client-Server Application Security

What happens when you design your own custom RSA protocol is that 1-18 months
afterwards, hopefully sooner but often later, you discover that you made a
mistake and your protocol had virtually no security. A good example is Salt
Stack. [Salt managed to deploy e=1 RSA][56].

[56]: http://www.cryptofails.com/post/70059600123/saltstack-rsa-e-d-1

It seems a little crazy to recommend TLS given its recent history:

* The Logjam DH negotiation attack
* The FREAK export cipher attack
* The POODLE CBC oracle attack
* The RC4 fiasco
* The CRIME compression attack
* The Lucky13 CBC padding oracle timing attack
* The BEAST CBC chained IV attack
* Heartbleed
* Renegotiation
* Triple Handshakes
* Compromised CAs

Here's why you should still use TLS for your custom transport problem:

* Many of these attacks only work against browsers, because they rely on the
  victim accepting and executing attacker-controlled Javascript in order to
  generate repeated known/chosen plaintexts. 
* Most of these attacks can be mitigated by hardcoding TLS 1.2+, ECDHE and
  AES-GCM. That sounds tricky, and it is, but it's less tricky than designing
  your own transport protocol with ECDHE and AES-GCM! 
* In a custom transport scenario, you don't need to depend on CAs: you can
  self-sign a certificate and ship it with your code, just like Colin suggests
  you do with RSA keys.

**Use:** TLS

**Avoid:**

1. Designing your own encrypted transport, which is a genuinely hard
   engineering problem;
2. Using TLS but in a default configuration, like, with "curl"
3. Using "curl"
4. IPSEC

### Online Backups

Of course, you should host your own backups in house. The best security is the
security where others just don't get access to your data.

The best solution, IMO, is OpenZFS. Not only do you get data integrity with
256-bit checksums, but you get redundancy, volume management, network
transport, and many other options, all for free. [FreeNAS][57] makes setting this up
trivial. [Setting it up with Debian GNU/Linux][58] isn't to difficult.

[57]: http://www.freenas.org/
[58]: https://pthree.org/2012/04/17/install-zfs-on-debian-gnulinux/

If using an online backup service, rather than hosting your own, use
[Tarsnap][59]. It's withstood the test of time.

[59]: https://www.tarsnap.com/

Alternatively, [Keybase][60] has its own keybase filesystem (KBFS) that
supports public, private, and team repositories. The [specification is
sound][61], but they only provide 10 GB for free, without any paid plans
currently. All data is end-to-end encrypted in your KBFS client before being
stored on the filesystem, using the NaCl library.

[60]: https://keybase.io/
[61]: https://keybase.io/docs/crypto/kbfs

**Use:**

1. OpenZFS
2. Tarsnap
3. Keybase

**Avoid:**

1. Google
2. Apple
3. Microsoft
4. Dropbox
5. Amazon S3