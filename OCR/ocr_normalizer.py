from PIL import Image, ImageDraw, ImageFont
import pytesseract

# Rendering image
def render_text_to_image(text, font_path, image_size, font_size):
    image = Image.new('RGB', image_size, color = (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)
    return image

text = "🇹 ᴛᴇꜱᴛ ᴄᴀꜱᴇ Fooxy "

font_path = "fonts/ARIAL.TTF"
image = render_text_to_image(text, font_path, (500, 100), 30)
image.save("image.png")  # This will display the image

# Applying OCR to image
extracted_text = pytesseract.image_to_string(image)

# OCR output
print("Extracted Text:", extracted_text)
