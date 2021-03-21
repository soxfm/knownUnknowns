# AES vs ChaCha20 Encryption Protocols
## Overview
---
> Why is ChaCha20 preferable over AES
---

- ChaCha20 is based on XOR(Addition-Rotation-XOR), which are cpu friendly instructions(making it more compatible throughout different cpu architectures: 32 and 64-bit).
- AES, uses binary fields for the S-box and Mixcolumns computations, which are generally implemented as a look-up table.
- **AES** : The use of a look-up table with an index derived from the secret makes general implementations vulnerable to cache-timing attacks. ChaCha20 is not vulnerable to such attacks. __ When, AES is implemented with AES-NI such vulnerability is also not present.)
- Generally speaking: given the AES protocol standard and widespread implementation it has become the gold standard in encryption. 
