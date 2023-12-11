import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(length, count):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

def main():
    try:
        print("Welcome to the Strong Password Generator!")
        print("This program generates strong, secure passwords.")

        while True:
            try:
                password_length = int(input("Enter the length of the password: "))
                num_passwords = int(input("Enter the number of passwords to generate: "))

                if password_length <= 0 or num_passwords <= 0:
                    print("Please enter valid values for length and count (greater than zero).")
                else:
                    generated_passwords = generate_multiple_passwords(password_length, num_passwords)
                    print("\nGenerated Passwords:")
                    for idx, password in enumerate(generated_passwords, start=1):
                        print(f"Password {idx}: {password}")
                    break
            except ValueError:
                print("Please enter valid integer values for length and count.")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
