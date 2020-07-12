import lyricsgenius
genius = lyricsgenius.Genius("G23EEDCAnKeA-0vI-sIzjw3LfXTnxOzaWuKCJ6100G3-0CPT_vy3X5tcw_81ByOw")
song = genius.search_song("Closer")
for line in song.lyrics.split("\n"):
    print(line)
