import os
import requests

from lib.genshin.datafiles.artifacts import ArtifactData, ArtifactPieceBonusesData, ArtifactSetData, SKIP_ARTIFACTS
from lib.genshin.datafiles.lang import LangData
from lib.genshin.utils import convert_id
from lib.genshin.sprite import ImageGenerator

dirname = os.path.dirname(__file__)
img_path = os.path.join(dirname, '../data/images/')

SLOT_DATA = {
    'EQUIP_RING': 'goblet',
    'EQUIP_NECKLACE': 'plume',
    'EQUIP_DRESS': 'circlet',
    'EQUIP_BRACER': 'flower',
    'EQUIP_SHOES': 'sands',
}

CUSTOM_NAMES_DATA = {
    'flower': '4',
    'plume': '2',
    'sands': '5',
    'goblet': '1',
    'circlet': '3',
}

set_data = ArtifactSetData()
sets_bonuses = ArtifactPieceBonusesData()
art_data = ArtifactData()
lang = LangData('EN')
items = {
    'flower': ['artifact-icon-unknown'],
    'plume': ['artifact-icon-unknown'],
    'sands': ['artifact-icon-unknown'],
    'goblet': ['artifact-icon-unknown'],
    'circlet': ['artifact-icon-unknown'],
}
images = {
    'flower': [f"{img_path}artifacts/UI_RelicIcon_Unknown_4.png"],
    'plume': [f"{img_path}artifacts/UI_RelicIcon_Unknown_2.png"],
    'sands': [f"{img_path}artifacts/UI_RelicIcon_Unknown_5.png"],
    'goblet': [f"{img_path}artifacts/UI_RelicIcon_Unknown_1.png"],
    'circlet': [f"{img_path}artifacts/UI_RelicIcon_Unknown_3.png"],
}

for art_set in set_data.get_list():
    if art_set['setId'] in SKIP_ARTIFACTS:
        continue
    if 'equipAffixId' not in art_set:
        continue

    bonus = sets_bonuses.bonuses_list(art_set['equipAffixId'])[0]
    name = lang.get(bonus['nameTextMapHash'])
    item_id = convert_id(name).replace('_', '-')

    for art_id in art_set['containsList']:
        item = art_data.get_item_by_field('id', art_id)
        slot = SLOT_DATA.get(item['equipType'])
        icon = item['icon']
        art_icon_name = item['icon']
        art_icon_path = f"{img_path}artifacts/{art_icon_name}.png"
        
        if not os.path.isfile(art_icon_path):
            image_url = f'https://gi.yatta.moe/assets/UI/reliquary/{art_icon_name}.png'
            image_data = requests.get(image_url).content
            with open(art_icon_path, 'wb') as art_icon_file:
                art_icon_file.write(image_data)

        if slot not in items:
            items[slot] = []
            images[slot] = []
        items[slot].append(f'artifact-icon-{item_id}.{slot}')
        images[slot].append(art_icon_path)

# for slot in SLOT_DATA.values():
#     items[slot].extend([
#         f'artifact-icon-long-nights-oath.{slot}',
#         f'artifact-icon-finale-of-the-deep-galleries.{slot}',
#     ])

# for slot, id in CUSTOM_NAMES_DATA.items():
#     images[slot].extend([
#         f"{img_path}artifacts/UI_RelicIcon_15039_{id}.png",
#         f"{img_path}artifacts/UI_RelicIcon_15040_{id}.png",
#     ])

for slot in items:
    image_gen = ImageGenerator(
        items=items[slot],
        images=images[slot],
        pack_name=f'artifacts_{slot}',
    )

    rules = [
        {'size': 24, 'class': f'sprite-artifact.{slot}.sprite-24'},
        {'size': 40, 'class': f'sprite-artifact.{slot}.sprite-40'},
        {'size': 60, 'class': f'sprite-artifact.{slot}.sprite-60'},
    ]

    for rule in rules:
        image_gen.generate_sprite(
            prefix='artifacts_',
            sprite_class=rule['class'],
            size=(rule['size'], rule['size']),
        )

    image_gen.save()
