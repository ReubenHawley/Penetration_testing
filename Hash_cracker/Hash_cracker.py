import hashlib

type_of_hash = str(input('Which hash would you like to decode? '))
file_path = str(input("Enter path to the passwords with which to bruteforce: "))
hash_to_decrypt = str(input("Enter hash to decrypt: "))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_obj = hashlib.md5(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found MD5 password: {line.strip()}')
                exit(0)
        if type_of_hash == 'sha1':
            hash_obj = hashlib.sha1(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found sha1 password: {line.strip()}')
                exit(0)
        if type_of_hash == 'sha224':
            hash_obj = hashlib.sha224(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found sha224 password: {line.strip()}')
                exit(0)
        if type_of_hash == 'sha384':
            hash_obj = hashlib.sha384(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found sha384 password: {line.strip()}')
                exit(0)
        if type_of_hash == 'sha256':
            hash_obj = hashlib.sha256(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found sha256 password: {line.strip()}')
                exit(0)
        if type_of_hash == 'sha512':
            hash_obj = hashlib.sha512(line.strip().encode())
            hashed_response = hash_obj.hexdigest()
            if hashed_response == hash_to_decrypt:
                print(f'found sha512 password: {line.strip()}')
                exit(0)
    print('Password not in file')
