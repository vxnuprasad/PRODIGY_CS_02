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
    with open("encryption_key.txt", "w") as key_file:
        key_file.write(key)

def load_key():
    if os.path.exists("encryption_key.txt"):
        with open("encryption_key.txt", "r") as key_file:
            return key_file.read().strip()
    return None

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixel_array = np.array(image)

    # Simple encryption: swap pixel values based on key
    height, width, channels = pixel_array.shape
    for i in range(height):
        for j in range(width):
            if (i + j) % len(key) == 0:  # Swap based on the key pattern
                # Swap with a pixel at a position determined by the key
                swap_i = (i + int(key) % height) % height
                swap_j = (j + int(key) % width) % width
                pixel_array[i, j], pixel_array[swap_i, swap_j] = pixel_array[swap_i, swap_j], pixel_array[i, j]

    encrypted_image = Image.fromarray(pixel_array)
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    stored_key = load_key()
    if stored_key is None or stored_key != key:
        print("Password does not match.")
        return  # Exit if the key does not match

    image = Image.open(image_path)
    pixel_array = np.array(image)

    # Simple decryption: swap pixel values back based on key
    height, width, channels = pixel_array.shape
    for i in range(height):
        for j in range(width):
            if (i + j) % len(key) == 0:  # Swap back based on the key pattern
                swap_i = (i + int(key) % height) % height
                swap_j = (j + int(key) % width) % width
                pixel_array[i, j], pixel_array[swap_i, swap_j] = pixel_array[swap_i, swap_j], pixel_array[i, j]

    decrypted_image = Image.fromarray(pixel_array)
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

def main():
    while True:
        print("Select an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            print("Exiting the program.")
            break
        
        image_path = input("Enter the path of the image: ")

        if choice == 'e':
            key = input("Enter an encryption key (numeric): ")
            save_key(key)
            encrypt_image(image_path, key)
        elif choice == 'd':
            key = input("Enter the decryption key: ")
            decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please select 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
