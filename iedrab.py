from PIL import Image
import numpy as np

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

def encrypt_decrypt_image(image_path, key, mode):
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
        encrypted_decrypted_image = np.bitwise_xor(image_array, key)

    # Convert back to an image
    result_image = Image.fromarray(encrypted_decrypted_image)

    return result_image

def save_image(image, output_path):
    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    while True:
        print("\nOptions:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '3':
            print("Exiting the program.")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice. Please choose again.")
            continue

        key = input("Enter a key for encryption/decryption: ")
        image_path = input("Enter the path of the image: ")

        if choice == '1':
            result_image = encrypt_decrypt_image(image_path, key, 'encrypt')
        elif choice == '2':
            result_image = encrypt_decrypt_image(image_path, key, 'decrypt')

        if result_image is not None:
            output_path = input("Enter the output image path (e.g., output.png): ")
            save_image(result_image, output_path)

if __name__ == "__main__":
    main()
