import hashlib


def hashing(pk):
    hash_object = hashlib.sha1(s.encode('utf-8')).hexdigest()
    return hash_object


s = "Python Bootcamp"

hashing(s)