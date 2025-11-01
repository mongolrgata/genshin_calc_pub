import os
import requests

from lib.genshin.datafiles.char import CharData, SKIP_CHARACTERS
from lib.genshin.datafiles.lang import LangData
from lib.genshin.utils import convert_id
from lib.genshin.sprite import ImageGenerator

dirname = os.path.dirname(__file__)
img_path = os.path.join(dirname, '../data/images/')

char_data = CharData()
lang = LangData('EN')
items = [
    'char-icon-unknown',
    'char-icon-empty',
]
images = [
    f'{img_path}chars/UI_Icon_Unknown.png',
    f'{img_path}chars/UI_Icon_Reset.png',
]

for char in char_data.get_list():
    if char['id'] in SKIP_CHARACTERS:
        continue
    char_name = lang.get(char['nameTextMapHash'])
    if char['id'] == 10000005:
        char_name += '_boy'
    elif char['id'] == 10000007:
        char_name += '_girl'
    char_id = convert_id(char_name).replace('_', '-')
    char_icon_name = char['iconName']
    char_icon_path = f'{img_path}chars/{char_icon_name}.png'

    items.append(f'char-icon-{char_id}')
    images.append(char_icon_path)

    if not os.path.isfile(char_icon_path):
        image_url = f'https://gi.yatta.moe/assets/UI/{char_icon_name}.png'
        image_data = requests.get(image_url).content
        with open(char_icon_path, 'wb') as char_icon_file:
            char_icon_file.write(image_data)

# items.extend([
#     'char-icon-ineffa',
# ])

# images.extend([
#     f'{img_path}chars/UI_AvatarIcon_Ineffa.png',
# ])

image_gen = ImageGenerator(
    items=items,
    images=images,
    pack_name='chars',
)

rules = [
    {'size': 24, 'class': 'sprite-char.sprite-24'},
    {'size': 40, 'class': 'sprite-char.sprite-40'},
    {'size': 60, 'class': 'sprite-char.sprite-60'},
]

image_gen.generate_individual((80, 80))

for rule in rules:
    image_gen.generate_sprite(
        prefix='char_',
        sprite_class=rule['class'],
        size=(rule['size'], rule['size']),
    )

image_gen.save()
