# About
Source code of Genshin Impact damage calculator https://genshin.aspirine.su/.

# Disclaimer
This project was not developed as open source and I am not a frontend developer. Keep it in mind when you reading code.

# Build
## How to build
1. npm ci
2. npm run build

## Environment
- Windows
- Python 3.6.8
- nodejs v16.15.0

# Notes
git clone https://gitlab.com/Dimbreath/AnimeGameData.git dimrepo  
pip install tinify  
pip install pillow

# Scripts
- new_bin/import_char.py  
генерация файлов char_names.csv, char_skills.csv и char_talents.csv в папке ./data/strings/generated
- new_bin/make_char_images.py  
генерация иконок персонажей в папке ./src/images/chars  
генерация коллажей с иконками персонажей в папке ./src/images/sprites  
генерация css-файла icons_chars.css в папке ./src/css/generated
