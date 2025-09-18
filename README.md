# 🌍✨ Text File Translator (Python)

This project is a simple **text file translator** built with Python using the [`googletrans`](https://pypi.org/project/googletrans/) library.  
It lets you **read a text file, translate it into another language, and save the result automatically**. 🚀  

---

## 🔥 Features
- 📂 Translate **whole text files** in seconds.  
- 🌐 Supports **100+ languages** (Google Translate).  
- 🖥️ Simple input prompts: just type your file name and languages.  
- 💾 Saves translation into `translated.txt`.  
- 🛡️ Handles missing file errors gracefully.  

---

## ⚙️ Requirements
- 🐍 Python **3.7+**  
- 📦 Install the translator library:  
```bash
pip install googletrans==4.0.0-rc1

▶️ How It Works

1️⃣ The program asks you for:

📄 The file name / path (e.g., input.txt).

🔤 The source language (e.g., en for English).

🌎 The target language (e.g., fr for French).

2️⃣ It reads your file and translates the text.
3️⃣ It creates a new file → translated.txt.
4️⃣ ✅ Done!

🖥️ Example Usage
File in the same folder
Enter your file name: input.txt
Enter your source language (example: en): en
Enter the language you want to translate to (example: fr): fr
✅ Translation saved to translated.txt

File in another folder
Enter your file name: C:\Users\YourName\Documents\story.txt
Enter your source language (example: en): en
Enter the language you want to translate to (example: es): es
✅ Translation saved to translated.txt

🌍 Language Codes

Here are some common language codes you can use:

🇬🇧 en → English

🇫🇷 fr → French

🇪🇸 es → Spanish

🇩🇪 de → German

🇸🇦 ar → Arabic

🇨🇳 zh-cn → Chinese (Simplified)

🇯🇵 ja → Japanese

🔗 Full ISO 639-1 Language Codes

📖 Example Input / Output

📄 input.txt

Once upon a time, there was a young boy named Alex.
He loved exploring the forest near his village.
One day, he found a small, injured bird under a tree.


📄 translated.txt (French fr)

Il était une fois, il y avait un jeune garçon nommé Alex.
Il aimait explorer la forêt près de son village.
Un jour, il a trouvé un petit oiseau blessé sous un arbre.

⚠️ Notes

❌ If the file is not found → File not found. Please check the file name and try again.

🌐 Internet connection is required (uses Google Translate API).

📄 By default, the result is saved to translated.txt.

✨ You can customize the script to generate filenames like translated_fr.txt.

📑 Support for PDF / Word documents.

🤖 Auto-detect source language.

📚 Translate multiple files at once.

👨‍💻 Author

Made with ❤️ in Python.
