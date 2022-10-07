import cs50
import csv

def main():
    min_tempo = cs50.get_int("Minimum tempo: ")
    max_tempo = cs50.get_int("Maximum tempo: ")

    playlist = []
    # TODO: Read songs from 2018_top100.csv into playlist
    with open("2018_top100.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if min_tempo <= float(row["tempo"]) <= max_tempo:
                playlist.append(row["name"])

    # TODO: Print song titles from playlist
    for song in playlist:
        print(song)

main()