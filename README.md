# manage passwords
collect passwords and save them as encrypted .txt file
decrypt when viewing

Encryption with Fernet
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"my deep dark secret")
    token
    b'...'
    f.decrypt(token)
    b'my deep dark secret'
