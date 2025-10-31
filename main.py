import itertools
import string
import pyperclip

def calculate_combinations(characters, length):
    num_characters = len(characters)
    total_combinations = num_characters ** length
    print(f"\n📊 Calculation Result:")
    print(f"   • Available characters: {num_characters}")
    print(f"   • Selected characters: {characters}")
    print(f"   • Length of each string: {length}")
    print(f"   • Total possible combinations: {total_combinations:,}")
    return total_combinations

def generate_all_strings():
    print("\n=== String Generator (All Possible Combinations) ===")
    
    quantity = int(input("How many strings do you want to generate? "))
    length = int(input("How many characters should each string have? "))
    
    use_uppercase = input("Include UPPERCASE letters? (y/n) ").lower() == "y"
    use_lowercase = input("Include lowercase letters? (y/n) ").lower() == "y"
    use_numbers = input("Include numbers? (y/n) ").lower() == "y"
    
    use_specials = input("Include special characters? (y/n) ").lower() == "y"
    special_characters = ""
    if use_specials:
        special_characters = input("Enter the special characters you want to use (e.g., _@#): ")
    
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if special_characters:
        characters += special_characters
    
    if not characters:
        print("⚠️ No character set selected!")
        return
    
    total_combinations = calculate_combinations(characters, length)
    
    if quantity > total_combinations:
        print(f"⚠️ WARNING: You requested {quantity} strings, but there are only {total_combinations:,} possible combinations!")
        print("   There will be repetition.")
    
    print(f"\n🔄 Generating up to {quantity} strings...\n")
    
    all_strings = []
    for i, t in enumerate(itertools.product(characters, repeat=length)):
        if i >= quantity:
            break
        s = "".join(t)
        all_strings.append(s)
        print(f"{i+1}: {s}")
    
    print(f"\n✅ Total strings generated: {len(all_strings)}")
    
    print("\nWhat do you want to do with the generated strings?")
    print("[1] Save to a .txt file")
    print("[2] Copy all to clipboard")
    print("[3] Nothing (just display)")
    choice = input("Choose (1/2/3): ")
    
    if choice == "1":
        file_name = input("Enter the file name (without extension): ") + ".txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(all_strings))
        print(f"💾 Strings saved to '{file_name}'.")
    elif choice == "2":
        pyperclip.copy("\n".join(all_strings))
        print("📋 Strings copied to clipboard!")

if __name__ == "__main__":
    generate_all_strings()
