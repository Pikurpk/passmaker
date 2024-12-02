import random
import string
from datetime import datetime
import os
import time
import pyfiglet  # For generating ASCII text

# ANSI escape codes for colors and background colors
BLACK_BG = '\033[40m'  # Black background
LIGHT_GRAY_TEXT = '\033[37m'  # Light gray text (for simulated opacity)
RESET = '\033[0m'  # Reset to default color and background
BOLD = '\033[1m'  # Bold text for the growing effect
RESET_BOLD = '\033[22m'  # Reset bold


# Function to calculate age
def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - int(birth_year)


# Function to generate a random password
def generate_random_password(first_name, last_name, birth_day, birth_month, birth_year, symbol, include_symbol,
                             min_len=6, max_len=10):
    # Calculate the age based on the birth year
    age = calculate_age(birth_year)

    # Generate random password structure
    structure_choice = random.choice(["name_age", "birthdate_age", "name", "birthdate"])

    # Start building the password based on the structure choice
    if structure_choice == "name_age":
        password_base = first_name + str(age)  # Name and age
    elif structure_choice == "birthdate_age":
        password_base = f"{birth_day}{birth_month}{birth_year}{age}"  # Birthdate and age
    elif structure_choice == "name":
        password_base = first_name  # Just name
    else:
        password_base = f"{birth_day}{birth_month}{birth_year}"  # Just birthdate

    # Optionally add the symbol
    if include_symbol:
        password_base += symbol

    # Randomly determine password length (between min_len and max_len)
    password_length = random.randint(min_len, max_len)

    # If the base password is shorter than the desired length, fill the remaining with random characters
    remaining_length = password_length - len(password_base)
    random_part = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    # Final password
    final_password = password_base + random_part
    return final_password


# Function to generate multiple passwords
def generate_multiple_passwords(count, first_name, last_name, birth_day, birth_month, birth_year, symbol,
                                include_symbol, min_len=6, max_len=10):
    passwords = []
    for _ in range(count):
        password = generate_random_password(first_name, last_name, birth_day, birth_month, birth_year, symbol,
                                            include_symbol, min_len, max_len)
        passwords.append(password)
    return passwords


# Function to simulate hacker-style animation with ASCII art text growing effect
def animate_hacker_mask(text, duration=2):
    # Use pyfiglet to create ASCII art from text
    ascii_art = pyfiglet.figlet_format(text, font="slant")  # Slant font gives a good hacker-style effect

    lines = ascii_art.split("\n")

    start_time = time.time()

    # Animate the text like it's being typed
    for i in range(1, len(lines) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for each new frame
        # Print progressively more of the ASCII art
        print(f"{LIGHT_GRAY_TEXT}{BLACK_BG}{''.join(lines[:i])}{RESET}")
        time.sleep(duration / len(lines))  # Control the speed of the typing effect

    time.sleep(0.5)  # Add a small delay before the next steps


# Function to display centered text with reduced opacity effect
def display_centered_text(text, width=80):
    # Calculate the padding required to center the text
    padding = (width - len(text)) // 2
    print(f"{LIGHT_GRAY_TEXT}{' ' * padding}{text}{RESET}")


# Main program to get user input and generate the passwords
os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for a fresh start

# Set black background
print(f"{BLACK_BG}{' ' * 80}{RESET}")  # Setting black background for the terminal screen

# Run the hacker-style animation before the main output
animate_hacker_mask("PikurPk", duration=2)

# Adding a blank line for some space after animation
print(f"{BLACK_BG}{" " * 80}{RESET}")

# Display the "PIKACHU.PK" text with reduced opacity in the center
display_centered_text("PIKACHU.PK")

# Adding a blank line for some space between the floating text and user inputs
print(f"{BLACK_BG}{" " * 80}{RESET}")

# Getting user input
print(f"{LIGHT_GRAY_TEXT}Enter your first name: {RESET}", end="")
first_name = input()
print(f"{LIGHT_GRAY_TEXT}Enter your last name: {RESET}", end="")
last_name = input()
print(f"{LIGHT_GRAY_TEXT}Enter your birth day (dd): {RESET}", end="")
birth_day = input()
print(f"{LIGHT_GRAY_TEXT}Enter your birth month (mm): {RESET}", end="")
birth_month = input()
print(f"{LIGHT_GRAY_TEXT}Enter your birth year (yyyy): {RESET}", end="")
birth_year = input()
print(f"{LIGHT_GRAY_TEXT}Enter a symbol (e.g., @, $, ., #): {RESET}", end="")
symbol = input()
print(f"{LIGHT_GRAY_TEXT}Do you want to include the symbol in the password? (yes/no): {RESET}", end="")
include_symbol = input().lower() == "yes"
print(f"{LIGHT_GRAY_TEXT}How many passwords do you want to generate? {RESET}", end="")
num_passwords = int(input())

# Allow user to specify the file path, remove quotes if any
print(f"{LIGHT_GRAY_TEXT}Enter the file path to save the passwords (e.g., C:\\Users\\YourName\\passwords.txt): {RESET}",
      end="")
file_path = input().strip('"')

# Generate multiple passwords
passwords = generate_multiple_passwords(num_passwords, first_name, last_name, birth_day, birth_month, birth_year,
                                        symbol, include_symbol)

# Save passwords to user-specified file
with open(file_path, "w") as file:
    for password in passwords:
        file.write(password + "\n")

# Display the result
print(f"{LIGHT_GRAY_TEXT}{num_passwords} passwords have been generated and saved to {file_path}.{RESET}")
