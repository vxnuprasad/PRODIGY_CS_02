from PIL import Image
import numpy as np
import os

# Banner for the program
banner = """
██╗███████╗██████╗░  ██████╗░░█████╗░██████╗░
██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
██║█████╗░░██║░░██║  ██████╔╝███████║██████╦╝
██║██╔══╝░░██║░░██║  ██╔══██╗██╔══██║██╔══██╗
██║███████╗██████╔╝  ██║░░██║██║░░██║██████╦╝
╚═╝╚══════╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
"""
print(banner)
print("------------- Image Encryption Tool By Techno-rabit --------------")

def save_key(key):
    """Save the encryption key to a file."""
    with open("encryption_key.txt", "w") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from a file."""
    if os.path.exists("encryption_key.txt"):
        with open("encryption_key.txt", "r") as key_file:
            return key_file.read().strip()
    return None

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Ensure key has the same shape as img_array
    key = np.resize(key, img_array.shape)

    # Encrypt each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Ensure key has the same shape as encrypted_array
    key = np.resize(key, encrypted_array.shape)

    # Decrypt each pixel using XOR with the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully as 'decrypted_image.png'.")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    while True:
        print("\nSelect an option:")
        print("1 - Encrypt an image")
        print("2 - Decrypt an image")
        print("q - Quit")
        
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            print("Exiting the program.")
            break

        if choice == '1':
            # Get image path and generate a random key for encryption
            image_path = input("Enter the path to the image file for encryption: ")
            key = input("Enter an encryption key (numeric): ")  # Get the key from the user
            save_key(key)  # Save the key to a file
            key_array = np.full((3,), int(key), dtype=np.uint8)  # Create a key array

            encrypt_image(image_path, key_array)  # Encrypt the image
            print("Exiting the program after encryption.")
            break  # Exit after encryption
        
        elif choice == '2':
            # Load the stored key for comparison
            stored_key = load_key()
            if stored_key is None:
                print("No stored key found. Please encrypt an image first.")
                continue
            
            # Get image path for decryption and key for verification
            encrypted_image_path = input("Enter the path to the encrypted image file: ")
            key = input("Enter the decryption key: ")

            if key != stored_key:
                print("Password does not match. Exiting the program.")
                break  # Exit if the key does not match

            key_array = np.full((3,), int(key), dtype=np.uint8)  # Create a key array
            decrypt_image(encrypted_image_path, key_array)  # Decrypt the image
            print("Exiting the program after decryption.")
            break  # Exit after decryption
        
        else:
            print("Invalid choice. Please select '1' to encrypt, '2' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
