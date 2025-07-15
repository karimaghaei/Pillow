from PIL import Image, ImageDraw, ImageFont
import os

# تصویر ورودی رو باز می‌کنیم
image_path = "images/sample.jpg"  # مسیر تصویرت رو بذار اینجا
output_path = "images/output.jpg"

# تصویر رو باز کن
image = Image.open(image_path)

# شیء Draw برای نوشتن روی تصویر
draw = ImageDraw.Draw(image)

# متن دلخواه
text = "سلام Vahid! 👋"

# فونت و اندازه (اگه فونت مخصوص داری می‌تونی مسیرشو بدی)
try:
    font = ImageFont.truetype("arial.ttf", size=40)
except:
    font = ImageFont.load_default()

# موقعیت قرارگیری متن
position = (50, 50)

# رنگ و نوشتن
draw.text(position, text, fill="red", font=font)

# ذخیره تصویر جدید
image.save(output_path)
print("تصویر با متن ذخیره شد در:", output_path)