===================
Encryption protocol
===================
GlobaLeaks implements an encryption protocol designed to implement a trade off between security and usability necessary to enable easy access and anonymous reporting by whistleblowers that is requirement for the most common whistleblowing scenarios.

The protocol is intended as well to provide reasonable security from attackers seizing the backend and attempting bruteforce decryption.

Encryption is implemented for each submission protecting questionnaire's answers, comments, attachments and involved metadata. The keys involved in the encryption are per-user and per-submission and only users to which the data was destinated could access the data. This mechanism guarantees that only the user could access the data. Users that would forget their password would lose access to data that won’t be accessible anymore. To handle with this condition the system implements as well `Key recovery`_ and `Key Escrow`_ mechanisms.

Encryption's workflow
#####################
* Users chooses a personal secure password at first login.
* The system creates a personal user keypair and stores it asymmetrically encrypted with a secret derived from the personal user password;
* The whistleblower files a report;
* The system assigns personal access credentials to the whistleblower;
* The system generates a symmetric key for the encryption of the report, the attached files and comments and the involved metadata and starts encrypting the data;
* The system generates an asymmetric keypair and store it symmetrically encrypted using a secret derived from the whistleblower access credentials;
* The system grants every involved recipient and the whistleblower access to the symmetric encryption key of the report by assigning each of the user an asymmetrically encrypted copy of the key;
* Users furtherly proceed exchanging information on the report by using their personal access credentials and unlocking their own personal asymmetric keys and symmetric keys of the accessed report.

Encryption's details
####################
Algorithms
---------------------
.. csv-table::
   :header: "Type", "Implementation"

   "Asymmetric encryption", "`Libsodium SealedBoxes <https://pynacl.readthedocs.io/en/stable/public/#nacl.public.SealedBox>`_, an encryption implementation that combines Curve25519, XSalsa20 and Poly1305 alghoritms."

   "Symmetric encryption", "`Libsodium SecretBoxes <https://pynacl.readthedocs.io/en/stable/secret/#nacl.secret.SecretBox>`_, an encryption implementation that combines XSalsa20 and Poly1305."

Users’ credentials
-----------------
The system used two different tyype of credentials depending on the user role:

.. csv-table::
   :header: "Credentials type", "User role"

   "Passwords", "For authenticated users identified by a username"
   "16-digits random receipts", "for anonymous Whistleblowers"

Assumptions:

* The system enforces authenticated users password quality based on strong password complexity rules.
* The system enforces expiration of receipts low the number of active receipts.

Users’ keys
-----------

.. csv-table::
   :header: "Type", "Generation", "Storage"

   "ECC Curve25519 keypair", "Generated by the backend at first user login for authenticated users and on submission for whistleblowers", "Keys are stored on the backend encrypted using symmetric encryption. The symmetric key used for encrypting users’ keys is derived from the users’ credentials using the KDF function `Argon2ID <https://password-hashing.net/argon2-specs.pdf>`_. The parameters for Argon2ID used for KDF are chosen stronger than the parameters one used for authentication of related user which the hash is stored. The parameters are chosen to require 128MB per Login and 1 second of computation."

Data encryption's keys
----------------------

.. csv-table::
   :header: "Type", "Generation", "Storage"

   "256 bit keys", "Generated by the backend for each report", "Keys and stored on backend filesystem  encrypted using asymmetric encryption by means of Users’ and Whistleblower’s keys respectively"

Key recovery
############
The system implements a key recovery system by means of a recovery key and symmetric encryption.

Upon generation of a user key, the private key is symmetrically encrypted with a randomly generated recovery key.

For usability reasons, this recovery is kept as well encrypted on the backend making it possible for logged users in possession of their password to retrieve and print their own account recovery key.

Key escrow
##########
The system implements an optional key escrow mechanism in order to limit data loss in case of users’ password loss.

The system could be configured to encrypt each user key upon generation with the key of selected administrators.

Administrators enabled with this capability are in possibility to support any internal user in case of password loss and issue password resets.