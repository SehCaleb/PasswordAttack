# PasswordAttack
Short code for a password trial and error password crack

import itertools
import string
import time

def brute_force_cracker(target_password, max_length=8, delay=0.1):
    chars = string.ascii_letters + string.digits + string.punctuation  #syntax for a string of characters i.e numbers , text , speacial characters
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            print(f"Trying: {guess}", end='\r') 
            if guess == target_password:
                print("\n" + "=" * 50)
                print(f"✅ Password found: {guess}")
                print("=" * 50)
                return guess
            time.sleep(delay)  # Simulate delay (avoids detection)
    
    print("\n❌ Failed to crack password (increase max_length?)")
    return None

if __name__ == "__main__":
    target = input("Enter a test password to crack: ")
    brute_force_cracker(target, max_length=4) 
