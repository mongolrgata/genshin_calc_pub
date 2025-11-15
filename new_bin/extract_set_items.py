from lib.genshin.datafiles.artifacts import ArtifactData

items = ArtifactData().get_list_by_field('setId', 15042)  # Silken Moon's Serenade
print(list(map(lambda i: i['id'], items)))
