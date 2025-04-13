import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        print("Error: No character types selected!")
        return None
    
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")
