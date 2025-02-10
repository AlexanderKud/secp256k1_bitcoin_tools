from ecdsa import SECP256k1
import random

def is_point_on_curve(x, y):
    # Check if (x, y) lies on the secp256k1 curve
    return (y**2) % SECP256k1.curve.p() == (x**3 + 7) % SECP256k1.curve.p()

def generate_random_point_on_curve():
    while True:
        # Randomly select (x, y) coordinates
        x = random.randint(1, SECP256k1.curve.p() - 1)
        #x = random.randint(1, 2**135)
        y_squared = (x**3 + 7) % SECP256k1.curve.p()
        # Check if there's a valid y-coordinate
        y = modular_sqrt(y_squared, SECP256k1.curve.p())
        if y is not None:
            return x, y

# Modular square root function
def modular_sqrt(a, p):
    if legendre_symbol(a, p) != 1:
        return None  # No square root exists
    else:
        return pow(a, (p + 1) // 4, p)

# Legendre symbol calculation
def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

# Example usage
iterations = 7
for i in range(iterations):
    random_point = generate_random_point_on_curve()
    #print(f"Random point on secp256k1 curve: {random_point}")
    print(f"Random point on secp256k1 curve")
    print(f'X: {hex(random_point[0])[2:].zfill(64)}')
    print(f'Y: {hex(random_point[1])[2:].zfill(64)}')
    print(is_point_on_curve(random_point[0], random_point[1]))
    print()
