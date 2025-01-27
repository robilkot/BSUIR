from Crypto.Util.number import getStrongPrime


FERMAT_NUMBERS = [65537, 257, 17]


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    f.close()
    return data


def write_file(filename, message):
    with open(filename, "w") as f:
        f.write(message)
    f.close()


def power_by_module(x, degree, p):
    result = x
    bit_degree = bin(degree)[3:]
    for i in bit_degree:
        result = ((result ** 2) * x) % p\
            if i == '1'\
            else (result ** 2) % p
    return result


def multiplicative_reciprocal(e, e_func):
    x, old_x, y, old_y = 0, 1, 1, 0
    r, old_r = e_func, e
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return old_x % e_func


def create_keys():
    p = getStrongPrime(1024)
    q = getStrongPrime(1024)
    while p == q:
        q = getStrongPrime(1024)

    n = p * q
    e_func = (p - 1) * (q - 1)
    e = 0
    for number in FERMAT_NUMBERS:
        if e_func % number != 0:
            e = number
            break

    d = multiplicative_reciprocal(e, e_func)

    write_file("open_key.txt", f"{n},{e}")
    write_file("secret_key.txt", f"{n},{d}")


def encrypt_message(message):
    n, e = read_file("open_key.txt").split(",")
    c = power_by_module(int(message), int(e), int(n))
    return c


def decrypt_message(encrypted_message_):
    n, d = read_file("secret_key.txt").split(",")
    return power_by_module(int(encrypted_message_), int(d), int(n))


def encrypt_signature(message):
    n, d = read_file("secret_key.txt").split(",")
    signature = power_by_module(int(message), int(d), int(n))
    return signature


def decrypt_signature(signature):
    n, e = read_file("open_key.txt").split(",")
    signed_message_ = power_by_module(int(signature), int(e), int(n))
    return signed_message_


create_keys()

original_message = int(read_file("orig_mes.txt"))

# Encrypt message using open key
encrypted_message = encrypt_message(original_message)

# Encrypt message using private key
decrypted_message = decrypt_message(encrypted_message)

# Sending pair to recipient
s_ = encrypt_signature(original_message)

# Receive message with signature
signed_message = decrypt_signature(s_)

# Validate signature
if signed_message == original_message:
    print("\nSignature does match")
else:
    print("\nSignature does NOT match")
