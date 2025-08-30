import qrcode
import os

def generate_qr_code(data, file_name, text=None):

    # Your specified save path
    save_path = r"D:/CODES/PYTHON/qr_code/qrcodes_generated"

    # Create directory if it doesn't exist
    # if not os.path.exists(save_path):
    #     os.makedirs(save_path)
    #     print(f"Created directory: {save_path}")

    # Create QR code with your original settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Handle text if provided
    if text:
        from PIL import Image, ImageDraw, ImageFont

        # Convert to RGB for text manipulation
        qr_img = img.convert('RGB')

        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        # Calculate text dimensions
        temp_img = Image.new('RGB', (1, 1))
        temp_draw = ImageDraw.Draw(temp_img)
        text_bbox = temp_draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Create new image with space for text
        qr_width, qr_height = qr_img.size
        total_width = max(qr_width, text_width + 20)
        total_height = qr_height + text_height + 40

        # Create final image
        final_img = Image.new('RGB', (total_width, total_height), 'white')

        # Paste QR code
        qr_x = (total_width - qr_width) // 2
        final_img.paste(qr_img, (qr_x, 10))

        # Add text
        draw = ImageDraw.Draw(final_img)
        text_x = (total_width - text_width) // 2
        text_y = qr_height + 20
        draw.text((text_x, text_y), text, font=font, fill='black')

        img = final_img

    # Ensure file name has .png extension
    if not file_name.endswith('.png'):
        file_name += '.png'

    # Create full file path
    full_path = os.path.join(save_path, file_name)

    # Save the image
    img.save(full_path)

    return full_path

if __name__ == "__main__":
    # credly
    generate_qr_code(
        "https://www.credly.com/users/jurg-charles-lim",
        "credly_jcl.png"
    )

    # LinkIn
    generate_qr_code(
        "https://www.linkedin.com/in/jurg-charles-lim-1a3235193/#education",
        "linkedIn_jcl.png"
    )

    print("QR codes saved to D:\\CODES\\PYTHON\\qr_code\\qrcodes_generated\\")
