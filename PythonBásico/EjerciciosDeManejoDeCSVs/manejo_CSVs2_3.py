import csv

def count_videogames_by_genre(file_path):
    genre_counts = {}

    
    with open(file_path,"r", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            genre = row['género'].strip()
            
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

        print("Géneros encontrados:")
        for genre in sorted(genre_counts.keys()):
            print(f"{genre}: {genre_counts[genre]}")

if __name__ == "__main__":
    count_videogames_by_genre("video_games.csv")
