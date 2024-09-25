from PIL import Image
import numpy as np
import hashlib
import sys

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
print("------- Image Encryption Tool By Techno-rabit -------")

def encrypt_decrypt_image(image_path, key, mode, original_key_hash=None):
    # Open the image
    try:
        image = Image.open(image_path)
    except IOError:
        print("Error: Could not open or find the image.")
        return

    # Convert image to numpy array
    image_array = np.array(image)

    # Convert the key into a byte array (to XOR with image data)
    key = np.array([ord(char) for char in key], dtype=np.uint8)

    # Resize the key to fit the image size
    key = np.resize(key, image_array.shape)

    # Perform XOR encryption/decryption
    if mode == 'encrypt':
        encrypted_decrypted_image = np.bitwise_xor(image_array, key)
    elif mode == 'decrypt':
        # Check if the provided decryption key hash matches the stored one
        provided_key_hash = hashlib.sha256(key).hexdigest()
        if provided_key_hash != original_key_hash:
            print("Error: Key doesn't match. Decryption failed.")
            return None
        encrypted_decrypted_image = np.bitwise_xor(image_array, key)

    # Convert back to an image
    result_image = Image.fromarray(encrypted_decrypted_image)

    return result_image

def save_image(image, output_path, key):
    # Save the image
    image.save(output_path)
    
    # Hash the key and save it alongside the image
    key_hash = hashlib.sha256(np.array([ord(char) for char in key], dtype=np.uint8)).hexdigest()
    with open(output_path + ".keyhash", 'w') as f:
        f.write(key_hash)

    print(f"Image and key hash saved to {output_path} and {output_path}.keyhash")

def load_key_hash(image_path):
    try:
        with open(image_path + ".keyhash", 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Error: Key hash not found for the given image.")
        return None

def main():
    while True:
        print("\nOptions:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '3':
            print("Exiting the program.")
            sys.exit()
        elif choice not in ['1', '2']:
            print("Invalid choice. Please choose again.")
            continue

        if choice == '1':
            key = input("Enter a key for encryption: ")
            image_path = input("Enter the path of the image: ")
            result_image = encrypt_decrypt_image(image_path, key, 'encrypt')
            if result_image is not None:
                output_path = input("Enter the output image path (e.g., output.png): ")
                save_image(result_image, output_path, key)
                print("Encryption completed successfully.")
                sys.exit()  # Exit the program after encryption
        elif choice == '2':
            print("Enter the key given during encryption.")
            key = input("Enter a key for decryption: ")
            image_path = input("Enter the path of the encrypted image: ")
            key_hash = load_key_hash(image_path)
            if key_hash:
                result_image = encrypt_decrypt_image(image_path, key, 'decrypt', original_key_hash=key_hash)
                if result_image is not None:
                    output_path = input("Enter the output image path (e.g., output.png): ")
                    result_image.save(output_path)
                    print(f"Decrypted image saved to {output_path}")
                    sys.exit()  # Exit the program after decryption

if __name__ == "__main__":
    main()
