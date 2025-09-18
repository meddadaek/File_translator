from googletrans import Translator

file = input("Enter your file name: ")
lon = input("Enter your source language (example: en): ")
dest = input("Enter the language you want to translate to (example: fr): ")

try:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

        translator = Translator()
        translation = translator.translate(text, src=lon, dest=dest)

        # Save into a new file
        output_file = "translated.txt"
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(translation.text)

        print(f"✅ Translation saved to {output_file}")

except FileNotFoundError:
    print("❌ File not found. Please check the file name and try again.")
