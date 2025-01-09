#hash_cracker.py
import hashlib
import itertools
import string
import time
from typing import Optional

class HashCracker:
    def __init__(self):
        self.common_passwords = [
            "password123", "12345678", "qwerty123",
            "letmein", "admin123", "welcome1",
            # Add more common passwords as needed
        ]
        self.charset = string.ascii_lowercase + string.digits
    
    def hash_password(self, password: str, algorithm: str = 'md5') -> str:
        """
        Hash a password using the specified algorithm
        """
        if algorithm == 'md5':
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == 'sha1':
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == 'sha256':
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    def dictionary_attack(self, target_hash: str, algorithm: str = 'md5') -> Optional[str]:
        """
        Attempt to crack hash using common passwords
        """
        print("Attempting dictionary attack...")
        
        for password in self.common_passwords:
            if self.hash_password(password, algorithm) == target_hash:
                return password
        
        return None
    
    def brute_force_attack(self, target_hash: str, max_length: int = 6, 
                          algorithm: str = 'md5') -> Optional[str]:
        """
        Attempt to crack hash using brute force
        WARNING: This is for educational purposes only!
        """
        print(f"Attempting brute force attack (max length: {max_length})...")
        
        # Try all possible combinations up to max_length
        for length in range(1, max_length + 1):
            print(f"Trying length {length}...")
            
            for guess in itertools.product(self.charset, repeat=length):
                password = ''.join(guess)
                if self.hash_password(password, algorithm) == target_hash:
                    return password
        
        return None
    
    def crack_hash(self, target_hash: str, algorithm: str = 'md5', 
                  max_length: int = 6) -> Optional[str]:
        """
        Attempt to crack a hash using multiple methods
        """
        start_time = time.time()
        
        # First try dictionary attack
        result = self.dictionary_attack(target_hash, algorithm)
        if result:
            elapsed = time.time() - start_time
            print(f"\nPassword found (dictionary attack) in {elapsed:.2f} seconds!")
            return result
        
        # If dictionary attack fails, try brute force
        result = self.brute_force_attack(target_hash, max_length, algorithm)
        if result:
            elapsed = time.time() - start_time
            print(f"\nPassword found (brute force) in {elapsed:.2f} seconds!")
            return result
        
        print("\nPassword not found!")
        return None

def main():
    cracker = HashCracker()
    
    # Menu
    while True:
        print("\nHash Cracker Menu:")
        print("1. Create hash from password")
        print("2. Attempt to crack hash")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == '1':
            password = input("Enter password to hash: ")
            algorithm = input("Enter algorithm (md5/sha1/sha256): ").lower()
            
            try:
                hash_value = cracker.hash_password(password, algorithm)
                print(f"\nHash: {hash_value}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            target_hash = input("Enter hash to crack: ")
            algorithm = input("Enter algorithm (md5/sha1/sha256): ").lower()
            max_length = int(input("Enter maximum password length to try: "))
            
            try:
                result = cracker.crack_hash(target_hash, algorithm, max_length)
                if result:
                    print(f"Cracked password: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
