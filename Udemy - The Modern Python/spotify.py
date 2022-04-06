global playlist
playlist = {
    'Title': 'Heal!',
    'Author': 'Ramin',
    'Songs': [
        {'Title': 'Ful Stop', 'Artist': 'Radiohead', 'Duration': 6.09},
        {'Title': 'AMOK', 'Artist': 'Atoms For Peace', 'Duration': 4.04},
        {'Title': 'Compliance', 'Artist': 'Muse', 'Duration': 5.12},
    ]
}


def playtime():
    i = 0
    play = []
    while i < len(playlist['Songs']):
        play.append(playlist['Songs'][i]['Duration'])
        i += 1
    print(f"{round(sum(play), 2)} Minutes")


playtime()

# length = 0
# for song in playlist['Songs']:
#     length += song['Duration']
# print(length)
