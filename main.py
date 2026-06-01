from pwdlib import PasswordHash

password = "1234567890"
password_hash = PasswordHash.recommended()
hash = password_hash.hash(password)
print("ハッシュ化したパスワード:")
print(hash) # => $argon2id$v=19$m=65536,t=3,p=4$NOQrOrcii43nLurtsUIDmQ$U6HTryNyb3OCNIMgSHTkDyMaRiWF2AzfLypJybYXOXA

result = password_hash.verify(password, hash)
print("パスワードの検証:")
print(result) # => True
