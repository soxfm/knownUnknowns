# Crypto Authentication
## GMAC | UMAC
## Galois Message Authentication Code
> In cryptography, Galois/Counter Mode (GCM) is a mode of operation for symmetric-key cryptographic block ciphers widely adopted for its performance. GCM throughput rates for state-of-the-art, high-speed communication channels can be achieved with inexpensive hardware resources.\[1] The operation is an authenticated encryption algorithm designed to provide both data authenticity (integrity) and confidentiality. GCM is defined for block ciphers with a block size of 128 bits. Galois Message Authentication Code (GMAC) is an authentication-only variant of the GCM which can form an incremental message authentication code. Both GCM and GMAC can accept initialization vectors of arbitrary length
> Different block cipher modes of operation can have significantly different performance and efficiency characteristics, even when used with the same block cipher. GCM can take full advantage of parallel processing and implementing GCM can make efficient use of an instruction pipeline or a hardware pipeline. The cipher block chaining (CBC) mode of operation incurs pipeline stalls that hamper its efficiency and performance.
### Basic Operation
Like in normal counter mode, blocks are numbered sequentially, and then this block number is combined with an initialization vector (IV) and encrypted with a block cipher E, usually AES. The result of this encryption is then XORed with the plaintext to produce the ciphertext. Like all counter modes, this is essentially a stream cipher, and so it is essential that a different IV is used for each stream that is encrypted.
The ciphertext blocks are considered coefficients of a polynomial which is then evaluated at a key-dependent point H, using finite field arithmetic. The result is then encrypted, producing an authentication tag that can be used to verify the integrity of the data. The encrypted text then contains the IV, ciphertext, and authentication tag. 
### Mathematical Basis
GCM combines the well-known counter mode of encryption with the new Galois mode of authentication. The key-feature is the ease of parallel-computation of the Galois field multiplication used for authentication. This feature permits higher throughput than encryption algorithms, like CBC, which use chaining modes. The GF(2128) field used is defined by the polynomial
x^{128}+x^{7}+x^{2}+x+1
The authentication tag is constructed by feeding blocks of data into the GHASH function and encrypting the result. This GHASH function is defined by
{\text{GHASH}}(H,A,C)=X_{m+n+1}_

### USE
GCM mode is used in the IEEE 802.1AE (MACsec) Ethernet security, IEEE 802.11ad (also dubbed WiGig), ANSI (INCITS) Fibre Channel Security Protocols (FC-SP), IEEE P1619.1 tape storage, IETF IPsec standards,[4][5] SSH[6], TLS 1.2[7][8] and TLS 1.3.[9] AES-GCM is included in the NSA Suite B Cryptography and its latest replacement in 2018 Commercial National Security Algorithm (CNSA) suite.[10] GCM mode is used in the SoftEther VPN server and client,[11] as well as OpenVPN since version 2.4.

### Performance 
GCM requires one block cipher operation and one 128-bit multiplication in the Galois field per each block (128 bit) of encrypted and authenticated data. The block cipher operations are easily pipelined or parallelized; the multiplication operations are easily pipelined and can be parallelized with some modest effort (either by parallelizing the actual operation, by adapting Horner's method per the original NIST submission, or both).
Intel has added the PCLMULQDQ instruction, highlighting its use for GCM.[12] In 2011, SPARC added the XMULX and XMULXHI instructions, which also perform 64 × 64 bit carry-less multiplication. In 2015, SPARC added the XMPMUL instruction, which performs XOR multiplication of much larger values, up to 2048 × 2048 bit input values producing a 4096-bit result. These instructions enable fast multiplication over GF(2n), and can be used with any field representation.
Impressive performance results are published for GCM on a number of platforms. Käsper and Schwabe described a "Faster and Timing-Attack Resistant AES-GCM"[13] that achieves 10.68 cycles per byte AES-GCM authenticated encryption on 64-bit Intel processors. Dai et al. report 3.5 cycles per byte for the same algorithm when using Intel's AES-NI and PCLMULQDQ instructions. Shay Gueron and Vlad Krasnov achieved 2.47 cycles per byte on the 3rd generation Intel processors. Appropriate patches were prepared for the OpenSSL and NSS libraries.[14]
When both authentication and encryption need to be performed on a message, a software implementation can achieve speed gains by overlapping the execution of those operations. Performance is increased by exploiting instruction-level parallelism by interleaving operations. This process is called function stitching,[15] and while in principle it can be applied to any combination of cryptographic algorithms, GCM is especially suitable. Manley and Gregg[16] show the ease of optimizing when using function stitching with GCM. They present a program generator that takes an annotated C version of a cryptographic algorithm and generates code that runs well on the target processor.
GCM has been criticized for example by Silicon Labs in the embedded world because the parallel processing isn't suited for performant use of cryptographic hardware engines and therefore reduces the performance of encryption for some of the most performance-sensitive devices.[17]

## UMAC
In cryptography, a message authentication code based on universal hashing, or UMAC, is a type of message authentication code (MAC) calculated choosing a hash function from a class of hash functions according to some secret (random) process and applying it to the message. The resulting digest or fingerprint is then encrypted to hide the identity of the hash function used. As with any MAC, it may be used to simultaneously verify both the data integrity and the authenticity of a message.
A specific type of UMAC, also commonly referred to just UMAC, is specified in RFC 4418, it has provable cryptographic strength and is usually a lot less computationally intensive than other MACs. UMAC's design is optimized for 32-bit architectures with SIMD support, with a performance of 1 CPU cycle per byte (cpb) with SIMD and 2 cpb without SIMD. A closely related variant of UMAC that is optimized for 64-bit architectures is given by VMAC, which has been submitted to the IETF as a draft (draft-krovetz-vmac-01) but never gathered enough attention for becoming a standardized RFC.

### Background
Let's say the hash function is chosen from a class of hash functions H, which maps messages into D, the set of possible message digests. This class is called universal if, for any distinct pair of messages, there are at most |H|/|D| functions that map them to the same member of D.
This means that if an attacker wants to replace one message with another and, from his point of view the hash function was chosen completely randomly, the probability that the UMAC will not detect his modification is at most 1/|D|.
But this definition is not strong enough — if the possible messages are 0 and 1, D={0,1} and H consists of the identity operation and not, H is universal. But even if the digest is encrypted by modular addition, the attacker can change the message and the digest at the same time and the receiver wouldn't know the difference.
Strongly universal hashing
A class of hash functions H that is good to use will make it difficult for an attacker to guess the correct digest d of a fake message f after intercepting one message a with digest c. In other words,
\Pr _{{h\in H}}[h(f)=d|h(a)=c]\,
needs to be very small, preferably 1/|D|.
It is easy to construct a class of hash functions when D is field. For example, if |D| is prime, all the operations are taken modulo |D|. The message a is then encoded as an n-dimensional vector over D (a1, a2, ..., an). H then has |D|n+1 members, each corresponding to an (n + 1)-dimensional vector over D (h0, h1, ..., hn). If we let
h(a)=h_{0}+\sum _{{i=1}}^{n}h_{i}a_{i}\,

# POLY1305
Poly1305 is a cryptographic message authentication code (MAC) created by Daniel J. Bernstein. It can be used to verify the data integrity and the authenticity of a message. A variant of Bernstein's Poly1305 that does not require AES has been standardized by the Internet Engineering Task Force in RFC 8439.

### Description 
The original proposal, Poly1305-AES, which uses AES block cipher to expand key, computes a 128-bit (16 bytes) authenticator of a variable-length message, using a 128-bit AES key, a 128-bit additional key (with 106 effective key bits), r, and a 128-bit nonce. The message is broken into 16-byte chunks which become coefficients of a polynomial in r, evaluated modulo the prime number 2130−5. The name is derived from this and the use of 2130−5 and the Advanced Encryption Standard. In NaCl Poly1305 is used with Salsa20 instead of AES, in TLS and SSH it is used with ChaCha20 keystream.
Google has selected Poly1305 along with Bernstein's ChaCha20 symmetric cipher as a replacement for RC4 in TLS/SSL, which is used for Internet security. Google's initial implementation is used in securing https (TLS/SSL) traffic between the Chrome browser on Android phones and Google's websites.[1] Use of ChaCha20/Poly1305 has been standardized in RFC 7905.
Shortly after Google's adoption for use in TLS, both ChaCha20 and Poly1305 support was added to OpenSSH via the chacha20-poly1305@openssh.com authenticated encryption cipher.[2][3] Subsequently, this made it possible for OpenSSH to remove its dependency on OpenSSL through a compile-time option.[4]

### Security
The security of Poly1305-AES is very close to the underlying AES block cipher algorithm. Consequently, the only way for an attacker to break Poly1305-AES is to break AES.
For instance, assuming that messages are packets up to 1024 bytes; that the attacker sees 264 messages authenticated under a Poly1305-AES key; that the attacker attempts a whopping 275 forgeries; and that the attacker cannot break AES with probability above δ; then, with probability at least 0.999999-δ, all the 275 are rejected.[5]