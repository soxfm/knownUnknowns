# Cryptography Concepts 
++ rewritten from https://developer.virgilsecurity.com/docs/e3kit/fundamnetals/cryptography++

### Encryption and Decryption 
Cryptography is the process of encoding a message or piece of information which can only be accessed   by authorized parties. The process of encrypting something in itself does not protect the actual message from being intercepted; however, what it does provide is an extended layer of security in case of an interception occurrence. ie.) Rendering the messages' content and/or information as unreadable/unintelligible. 
Through the use of mathematical algorithms; a **cypher** encrypts a piece of text into **cyphertext**, which can only be read if decrypted by its designated key. "It is in principle possible to decrypt the message without possessing the key, but, for a well-designed encryption scheme, considerable computational resources and skills are required."

### Symmetric Encryption
Symmetric-key encryption[[a]] is when the same [cryptographic key] is used for both encryption of [plaintext] and decryption of [ciphertext]. The endpoints will either have duplicates of the key, or they will pass the key back and forth.[[1]] The keys, in practice, represent a [shared secret] between two or more parties that can be used to maintain a private information link. This requirement that both parties have access to the secret key is one of the main drawbacks of symmetric key encryption, in comparison to [public-key encryption] (also known as asymmetric key encryption), because the key must somehow be shared secretly. 
> eg.) an example of **Symmetric encryption** is the WPA-PSK(wifi preshared password key which is utilized in order to authenticate users to their pertaining access points.)

### Asymmetric Encryption
Public-key cryptography, or asymmetric cryptography, is a cryptographic system that uses pairs of two distinct keys: a public key which may be disseminated widely, and a private key which is known only to the owner. The generation of such keys depends on cryptographic algorithms based on mathematical problems to produce one-way functions.

Effective security requires keeping the private key private, but the public key can be openly distributed without compromising security.[1] In such a system, any person can encrypt a message using the receiver's public key, but that encrypted message can only be decrypted with the receiver's private key.
> e.g) SecureShell(SSH) Client and remote Host Connection are an example of asymmetric encryption.
#### Public Keys
Within the **asymmetric encryption** system; the usage of _public keys_ is widely and commonly accepted. __Public Keys__ represent a user's identity and are utilized in order  to confirm that such  user is the designated recipient of a message. Each user's _Public Key's_ have a corresponding private key (which; should only be available to the user himself); -- and  is utilized in order to decrypt the message. 
> To make asymmetric encryption system work, there has to be a central organizing party or system to make the public keys available to all participants, and ensure that the public keys and private keys work together, like a PKI.

#### Private Keys
In an asymmetric encryption system, private keys, unlike public keys, need to be kept secret in the user's device. They are used to unscramble ciphertext generated by the corresponding public key into plaintext.

In a chat application, when Bob receives a message from Alice, he decrypts the ciphertext message with his private key and reads it.

Because anyone with the private key can decrypt a message encrypted with that private key's public key, the strength of an asymmetric encryption system depends on how well the private key is protected from unauthorized access. Only the end user should have access the private key, and not the system developer or any other party. It should be generated on the user’s device and plaintext private keys should not be stored within any system or database that also contains any data that was encrypted for that private key. There can be no proverbial “backdoor.” access to the private key for anyone. With Virgil Security’s zero knowledge system, the end user’s private key is generated locally by the Virgil SDK on the user’s device upon sign-up or sign-in, and will remain stored locally on that device. This allows a user to decrypt encrypted data on this device where the private key is stored.

#### Digital Security

A digital signature is a mathematical scheme for verifying the authenticity of digital messages or documents. A valid digital signature gives a recipient reason to believe that the message was created by a known sender (authentication), that the sender cannot deny having sent the message (non-repudiation), and that the message was not altered in transit (integrity).[1]

Digital signatures are a standard element of most cryptographic protocol suites, and are commonly used for software distribution, financial transactions, contract management software, and in other cases where it is important to detect forgery or tampering.

#### Perfect Forward Secrecy 
Adding Perfect Forward Secrecy (PFS) to your encrypted communication prevents a possibly compromised long-term secret key from affecting the confidentiality of past and future communications. This is only supported by E3Kit's Double Ratchet Encryption method.
----
### BrainKey Concept
As it exists today, end-to-end encryption is mostly device-based, because that has been the surest way to both verify that a user is who they say they are and to safeguard against large-scale breaches. But that also makes practical usage frustrating for users. A real life reality is that we often switch phones or need to log in from a friend's computer, which is tricky with a product using end-to-end encryption and can lead to security shortcuts in favor of convenience.

Brainkey by Virgil Security is a strong cryptographic key based on a user-generated password, and is used to encrypt a user's private key in the Virgil Cloud. Users can then regenerate their original private key on multiple devices, allowing access to their encrypted data from new browser sessions or devices and preventing permanent loss of encrypted data if the original device is lost. This functionality is already baked in Virgil E3Kit, particularly Brainkey is used in the Key Backup functions.

Brainkey works with Pythia, designed by Adam Everspaugh and Rahul Chaterjee, University of Wisconsin–Madison; Samuel Scott, University of London; Ari Juels and Thomas Ristenpart, Cornell Tech. Take a look at the Virgil Security Pythia whitepaper for more information about the technical details.