# AES Encrypt / Decrypt Pattern Design
# Simple Python Code implementation of core concepts

---

## Realworld Python Examples of Encryption Decryption Modules written in python

```python
import pyaes, pbkdf2, binascii, os, secrets
# Encode pass with 256AES-bit Encryption.
password= "secret-shit-example-sample"
passwordSalt= os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))
```

```text
<from python repl std output>
AES encryption key: b'a407252ff0d492b93db44d3ddd2f24d4943829b15e03d4c85948cdccd94f1194'
```

The derived **key** consists of **64 hex digits** \(32 bytes\), which represents a **256-bit** integer number. It will be different if you run the above code several times, because a random salt is used every time. If you use the same salt, the same key will be derived.

### AES Encryption \(CTR Block Mode\)

Next, generate a **random 256-bit initial vector \(IV\)** for the AES CTR block mode and perform the **AES-256-CTR encryption**:

```python
# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
iv = secrets.randbits(256)
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted:', binascii.hexlify(ciphertext))
```

``text
Encrypted: b'53022cf12c5959ddf3e733128930dd3d52e3ea'
```

The **ciphertext** consists of **38 hex digits** \(19 bytes, 152 bits\). This is the size of the input data, the message `Text for encryption`.

Note that after AES-CTR encryption the **initial vector \(IV\)** should be stored along with the ciphertext, because without it, the decryption will be impossible. The **IV** should be randomly generated for each AES encryption \(not hard-coded\) for higher security.

Note also that if you encrypt the same **plaintext** with the same encryption **key** several times, the output will be **different** every time, due to the randomness in the **IV**. This is intended behavior and it increases the security, e.g. resistance to dictionary attacks.

### AES Decryption \(CTR Block Mode\)

Now let's see how to **decrypt a ciphertext** using the AES-CTR-256 algorithm. The input consists of **ciphertext** + encryption **key** + the **IV** for the CTR counter. The output is the original **plaintext**. The code is pretty simple:

```python
# Decrypt the ciphertext with the given key:
#   plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('Decrypted:', decrypted)
```

Note also that the above code **cannot detect wrong key**, wrong **ciphertext** or wrong **IV**. If you use an incorrect key to decrypt the ciphertext, you will get a wrong unreadable text. This is clearly visible by the code below:

```python
key = os.urandom(32)   # random decryption key
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
print('Wrongly decrypted:', aes.decrypt(ciphertext))
```


#### PyCryptodome Library

```python
from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

secretKey = os.urandom(32)  # 256-bit random encryption key
print("Encryption key:", binascii.hexlify(secretKey))

msg = b'Message for AES-256-GCM + Scrypt encryption'
encryptedMsg = encrypt_AES_GCM(msg, secretKey)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'aesIV': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
print("decryptedMsg", decryptedMsg)
```

#### AES-256-GCM + Scrypt Example

Now let's give a more complex example: **AES encryption of text by text password**. We shall use the authenticated encryption construction **AES-256-GCM**, combined with **Scrypt** key derivation:

```python
from Crypto.Cipher import AES
import scrypt, os, binascii

def encrypt_AES_GCM(msg, password):
    kdfSalt = os.urandom(16)
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (kdfSalt, ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, password):
    (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

msg = b'Message for AES-256-GCM + Scrypt encryption'
password = b's3kr3tp4ssw0rd'
encryptedMsg = encrypt_AES_GCM(msg, password)
print("encryptedMsg", {
    'kdfSalt': binascii.hexlify(encryptedMsg[0]),
    'ciphertext': binascii.hexlify(encryptedMsg[1]),
    'aesIV': binascii.hexlify(encryptedMsg[2]),
    'authTag': binascii.hexlify(encryptedMsg[3])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
print("decryptedMsg", decryptedMsg)
```

The **output** from the above code looks like this:

```text
encryptedMsg {'kdfSalt': b'2dd0b783290747ba62a63fc53591170d', 'ciphertext': b'223ed888dcd216dcd40c47ff7cdaa7fd7eab65f4f0405350a43c5cad5b6b47b527c709edec29d7d6967518', 'aesIV': b'7f114d946c77508ed2e6afe652c78f21', 'authTag': b'e84a14b9542320a0b1473141c989c48f'}
decryptedMsg b'Message for AES-256-GCM + Scrypt encryption'
```


