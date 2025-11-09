from lib.genshin.datafiles.artifacts import ArtifactData

items = ArtifactData().get_list_by_field('setId', 15041)  # Night of the Sky's Unveiling
print(list(map(lambda i: i['id'], items)))
