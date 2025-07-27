import qrcode

def generate_qr_code(data, filename="default_qr.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    qr.show()
    print(f"QR Code saved as {filename}")

def create_qr_code_with_input():
    """Takes user details and generates a QR code."""
    try:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        number = input("Enter your number: ")

        data = f"NAME: {name}, AGE: {age}, EMAIL: {email}, NUMBER: {number}"
        qr = qrcode.QRCode(version=5, box_size=5, border=2)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        filename = "user_details_qr.png"
        img.save(filename)
        img.show()
        print(f"QR Code with user details saved as {filename}")
    except Exception as e:
        print("Error:", e)

def generate_qr_for_url():
    """Generates a QR code for a given URL."""
    url = input("Enter the URL: ")
    qr = qrcode.QRCode(version=5, box_size=5, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    filename = "url_qr.png"
    img.save(filename)
    img.show()
    print(f"QR Code for URL saved as {filename}")

def main():
    print("\nQR Code Generator")
    print("1. Generate QR Code (default text)")
    print("2. Generate QR Code with User Input")
    print("3. Generate QR Code for a URL")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        generate_qr_code("Hello, World!", "default_text_qr.png")
    elif choice == '2':
        create_qr_code_with_input()
    elif choice == '3':
        generate_qr_for_url()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
