# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048) #CREA UNA COPPIA DI CHIAVI
# print(key_pair.export_key()) #STAMPIAMO LA CHIAVE PRIVATA
# public_key = key_pair.publickey() #STAMPIAMO LA CHIAVE PUBLICA
# print(public_key.export_key())
# exit(0)

sPriv ="-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA1860g4EdDj175BImYOe1ZPLhBr5KfNbvW6xyJQGfGaOHB6hk\nmEpIWXquibfZ9PGyr9gDe/9xAeqD1A93RceKUL7poHBOLjtRypgysokeJkRnYAsb\nWa2pTQ9GaxGxHQClZ3RDnvA32J8J5e9224VkL/bZKn7ohd0qnXBxVg67lUMUvP9w\nOVOyp4pq8vHMUaKO118ANrPDW4V+x6AKKY/JBCw0L+BRb6T52hUmCGzA6OVYUiCr\nbqi7h6z7i+Drc0Peg1csU2s2LChNeb/3qFydDsaH36fzWT2lMHdyIbdKLUuAZQvY\ncj5Q8FnMLsz+8D8UUxA42DDqlBpWWiUmls/LdQIDAQABAoIBAA3QUme0hQqbTunb\na496ZXcPwO2wko4JKAsjL69Euk1m1UbdNYs1/gmUO8Xe+dme+wQcfKScRjyMKWIS\nl1zlF+pxPf0iEy8MZwDj2yLoegCTElbofxivcA3Zs3U5DbBAkVXc8FMlJz37eCO6\nv03v7OjRETeSJgojjQ3E28xZZxJ3uar5gDFHY72SkjH0R0hktxgrwEGuYxl62/a0\nqtUGmJcsUURmJK0nt0LoRrT6HTq0CGZtLF4cme8x/4CLkCU1DnpcezMXm85h2nKg\n7fKQDb/xmjGbrAk6VRao2L5ouaPv3jnJOuOpMgwW7wy4QLTZIE58O4ouuEjtAeR4\nXMRXFWUCgYEA5LoE5Nu5Xry8wKqN4ZPCv5XK0M4FTB4GRLsDnxgjfjIgMilOjpYI\njjbQbAt1cS6P08KmOCmxxmmGTT7arpSmRJtV0MqvlU0eb8B0vuez+GJGGmY3qvzv\n1kmv/Z2euUrV04VpSbInavpf0OwfHdnEZzSlFBAAfHfJyukL34oqLqcCgYEA8YpS\naQWhWDD2kOzih4j3NqO3bnt/u+bIbgITgZri4ycutEwNRWzmyNiSUBgiE8/7YKZT\n5R/spDYEGR9fqIghftjAZIfj6T9bWEsugThjybdXty4FFVmJC1EWs7jqPrRa0Hjm\n7Osq/krdDBBBC61X4e3e6BkIEGXU+ufG4RhANIMCgYEAhpKH1JsOepXzPCxc4+7K\n82vPc4DzjvBPYdria5WJNHOLi9fP14agrAPGJvuq8pehmcb5gyvM498sXIBxq6vc\nE5uNJxZJrj88fCWwyq2KrsYrVtbzQ9Aj0GF0gXRecch8/EGPTAPcu01qWILEYAzD\nSLGpup8bmh/kg1UQXkptPRsCgYEA5nvQgcjOmkI2tjplO2H2TJxS6ElOrTXeoiK3\nDGCJCqsUBRXhQBNX8eW/UFCHDBLV0/dDbQtWm6ezp2lptX8ZP1qD1Cpbz/IWLx2m\npcXyasTaHcD7NtE2VacuG5djZyxg0DfeW8tYPkmfvugvuX3Ss5NxtlZUfJk/b6EG\nBTtH4RMCgYBjYyUZov1cfBym8kL99wiwpHgsjsPIS35rVgC+dUVS3unUUKGyvVGb\n/BEtzQFyG9DimICoI+2EzMoaPJRuEKmEcvDUBr7a1nKZGQqWUi0PSfulhbcncsk2\n0w4nsjWRTKK003Vqe0CqFqJBbTltgHBqMCUJwoajjWC2mQ/kvbbPIg==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1860g4EdDj175BImYOe1\nZPLhBr5KfNbvW6xyJQGfGaOHB6hkmEpIWXquibfZ9PGyr9gDe/9xAeqD1A93RceK\nUL7poHBOLjtRypgysokeJkRnYAsbWa2pTQ9GaxGxHQClZ3RDnvA32J8J5e9224Vk\nL/bZKn7ohd0qnXBxVg67lUMUvP9wOVOyp4pq8vHMUaKO118ANrPDW4V+x6AKKY/J\nBCw0L+BRb6T52hUmCGzA6OVYUiCrbqi7h6z7i+Drc0Peg1csU2s2LChNeb/3qFyd\nDsaH36fzWT2lMHdyIbdKLUuAZQvYcj5Q8FnMLsz+8D8UUxA42DDqlBpWWiUmls/L\ndQIDAQAB\n-----END PUBLIC KEY-----"
sPubAle="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1OOZigoOuxZh5eNLhfmg\nSXftsct3wy9z7Uxk2t7tU4XCIVQ8qxOYddOk5Blv/OvAIxKJjJTP9vB7KKDpefLw\nrfP1I2vfTJIjSltX13T0LiwFviCZXmoOvmkSz9Fv89v0o8pSfavXyNpI3BShOy25\nl4Q+kOcuE8vL7LKuP8GnWlPFtfapcbFJfEe+Rda8htuA1b7c4Bpd+Pw42tZw/FWK\nw3lv6BSEuf82bzk7MK0J43nyJW4PXsruur0diP+/iPiMFwQJGkzGFD6dbYOFoRcY\nzjIBuhDc/YVxL/JRvkwubRZEqePbsoL/03ovFTknT1ymu0LwsAwbp7P2H2Lfp9Jf\n/wIDAQAB\n-----END PUBLIC KEY-----"
sPubLuca = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0yThh9uoOWQD5Go+3B4p\n6LRR8MOG/0fkMJrCYMbwK3TgLvIa/D/QnEtnLSa6CqwQlbL8QzCcLzqdxcux5QCf\nluwJChG2w87InAo6V/5roFc7BWei2sF68qQr3SGriNrHi7+DyYvkyeZfln/ukVFl\nA+EE2PoGMcP/2BsnW+9Z3mrDFgC+C57YOCLiNd1L1Fax9nq9FUuM7AbR3yCNkM/B\ntPDUrCJFoRkqLEbknVFIUjZyFjjL4NQh4yIJ8C73UcHl8bgTxZbzixU9evYyC1lx\n/RopnFnKpSz+I2LCHINUIcURDQYUi8b+zYpqLCJF8ZccLORofuswz6WZ1CfTzKXq\nBwIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_ale = RSA.import_key(sPubAle)
public_Luca = RSA.import_key(sPubLuca)


# Function to encrypt message
def encrypt_message(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   encrypted_message = cipher.encrypt(message.encode("utf-8"))
   return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
   return decrypted_message.decode("utf-8")


# # Example usage
# message = "This is a secret message"
# encrypted_message = encrypt_message(message, public_key)
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)

# # Decriptazione messaggio alessandro
# encrypted_message = "PEnG40pLHU+5z6gXoWdqMujZ/XDW1vG+j5MALgdN4L1OwbAX1x64svXZs/dlleA/Iw4P7hgij/0JeWkvT5pXuBkH12IpvkVwRcSgGRKVxglHmMR5bOxO0OpV+1mseV2DR9y4L397cx4qvWtSj6HvMNIYErc+qAho7BP/KE9gwqOc5YYwVjMXqVAUnuaftrbUJJbtGDz8jGtaHdGwlvEtZyeY0/BR284QJTGlEcWrai90CLD186tskw3ip7DkzotiQjzKyBu8DYfsXgPE45zVx1tqEfno67YEhgS/inzCh63d3YGhF62clQk5sEbwqhw7ZNOMxEJjAutf1/Dxf/jbIA=="
# decrypted_message = decrypt_message(encrypted_message, key_pair)
# print("Decrypted Message:", decrypted_message)

#criptazione messaggio di risposta per ale
message = "ti stai leggendi  tower of palle?"
encrypted_message = encrypt_message(message, public_Luca)
print("Encrypted Message:", encrypted_message)

