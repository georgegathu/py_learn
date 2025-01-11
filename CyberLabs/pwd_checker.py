import re
import getpass
from typing import Tuple

class PasswordStrengthChecker:
    def __init__(self):
        self.min_length = 8
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def check_strength(self, password: str) -> Tuple[bool, list]:
        """
        Check password strength against multiple criteria
        Returns: (is_strong, list of failures)
        """
        failures = []
        
        # Check length
        if len(password) < self.min_length:
            failures.append(f"Password must be at least {self.min_length} characters long")
        
        # Check for uppercase
        if not any(c.isupper() for c in password):
            failures.append("Password must contain at least one uppercase letter")
        
        # Check for lowercase
        if not any(c.islower() for c in password):
            failures.append("Password must contain at least one lowercase letter")
        
        # Check for numbers
        if not any(c.isdigit() for c in password):
            failures.append("Password must contain at least one number")
        
        # Check for special characters
        if not any(c in self.special_chars for c in password):
            failures.append("Password must contain at least one special character")
        
        # Check for common patterns
        common_patterns = [
            r'12345',
            r'qwerty',
            r'password',
            r'admin',
            r'letmein',
            r'welcome'
        ]
        
        for pattern in common_patterns:
            if re.search(pattern, password.lower()):
                failures.append(f"Password contains common pattern: {pattern}")
        
        # Calculate entropy score (basic implementation)
        entropy = self._calculate_entropy(password)
        if entropy < 3.0:
            failures.append("Password is not complex enough")
        
        return len(failures) == 0, failures
    
    def _calculate_entropy(self, password: str) -> float:
        """
        Calculate basic entropy score for password
        Higher score = more complex password
        """
        char_sets = {
            'uppercase': len([c for c in password if c.isupper()]),
            'lowercase': len([c for c in password if c.islower()]),
            'numbers': len([c for c in password if c.isdigit()]),
            'special': len([c for c in password if c in self.special_chars])
        }
        
        # Calculate diversity score
        used_sets = sum(1 for count in char_sets.values() if count > 0)
        length_score = len(password) / self.min_length
        
        return used_sets * length_score

def main():
    checker = PasswordStrengthChecker()
    
    while True:
        print("\nPassword Strength Checker")
        print("Enter 'q' to quit")
        
        # Use getpass to hide password input
        password = getpass.getpass("Enter password to check: ")
        
        if password.lower() == 'q':
            break
        
        is_strong, failures = checker.check_strength(password)
        
        print("\nPassword Strength Analysis:")
        if is_strong:
            print("✅ Password meets all security requirements!")
        else:
            print("❌ Password is weak. Please address the following:")
            for failure in failures:
                print(f"  • {failure}")
        
        print("\nPassword Length:", len(password))

if __name__ == "__main__":
    main()
