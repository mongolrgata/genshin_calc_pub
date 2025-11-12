# About
Source code of Genshin Impact damage calculator https://genshin.aspirine.su/.

# Build
## How to build
1. npm ci
2. npm run build

## Environment
- Windows
- Python 3.6.8
- nodejs v16.15.0

## Additional dependencies
git clone https://gitlab.com/Dimbreath/AnimeGameData.git dimrepo  
pip install tinify  
pip install pillow

# Scripts
- bin/**img.sh**  
shell-скрипт предназначенный для последовательной загрузки и обработке изображений по переданным URL-адресам
- bin/**gen_string_table.py**  
генерация словарей eng.js и rus.js в папке ./src/js/lang  
при работе скрипта учитывается содержимое csv-файлов в папке ./data/strings
- new_bin/**import_char.py**  
генерация файлов char_names.csv, char_skills.csv и char_talents.csv в папке ./data/strings/generated
генерация файла char_texts.txt в папке ./data/raw  
при работе скрипта учитываются настройки шаблонов в папке ./new_bin/lib/genshin/strings/templates/talents/, а также содержимое файлов ./dimrepo/TextMap/TextMapEN.json и ./dimrepo/TextMap/TextMapRU.json
- new_bin/**make_char_images.py**  
выгрузка иконок персонажей в папку ./data/images/chars 
генерация иконок персонажей в папке ./src/images/chars  
генерация коллажей с иконками персонажей в папке ./src/images/sprites  
генерация css-файла icons_chars.css в папке ./src/css/generated
- new_bin/**import_artifacts.py**  
генерация файлов artifact_set_names.csv (названия наборов артефактов) и artifact_set_bonuses.csv (названия и описания бонусов наборов артефактов)  
при работе скрипта учитываются настройки шаблонов в модулях artifacts_eng.py, artifacts_rus.py и names.py
- new_bin/**make_artifact_images.py**  
выгрузка иконок артефактов в папку ./data/images/artifacts  
генерация коллажей с иконками артефактов в папке ./src/images/sprites  
генерация css-файлов icons_artifacts_***.css в папке ./src/css/generated
- new_bin/**extract_set_items.py**  
получение списка itemIds для заданного набора артефактов  
требуется при создании экземпляра класса ArtifactSet

# TODO
- проверить необходимость в скрипте bin/img.sh
- проверить необходимость в папке ./src/images/artifacts
