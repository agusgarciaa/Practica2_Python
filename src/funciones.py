def count_lines(text): 
    lines = text.split("\n")
    return len(lines)


def count_words(text):
    words = text.split()
    return len(words)


def average_words(text):
    total = 0
    lines = text.split("\n")
    
    for line in lines:
        total += count_words(line)
        
    div = count_lines(text)
    average = total/div
    return average


def above_average(text):
    filtered_lines = []
    average = average_words(text)
    lines = text.split("\n")
    
    for line in lines:
        if count_words(line) > average:
            filtered_lines.append(line)
            
    return filtered_lines


def to_seconds(duration):
    mins, secs = duration.split(":")
    mins = int(mins)
    secs = int(secs)
    total_seconds = mins * 60 + secs
    return total_seconds


def song_playtime(song):
    time = song["duration"]
    total_seconds = to_seconds(time)
    return total_seconds


def total_playtime(playlist):
    total = 0
    for song in playlist:
        total += song_playtime(song)
    return total
        

def max_playtime(playlist):
    max_playtime = 0
    for song in playlist:
        duration = song_playtime(song)
        
        if duration > max_playtime:
            max_playtime = duration
            max_song = song
    return max_song
        

def min_playtime(playlist):
    min_playtime = 999999
    for song in playlist:
        duration = song_playtime(song)
        
        if duration < min_playtime:
            min_playtime = duration
            min_song = song
    return min_song


def filter_spoilers(review): 
    spoilers = input("Ingrese las palabras spoiler (separadas por coma): ")
    spoiler_list = [spoiler.strip() for spoiler in spoilers.split(",")]
    review_upper = review.upper()  # hacemos una versión en mayúsculas
    for word in spoiler_list:
        word_upper = word.upper()
        if word_upper in review_upper:
            start = 0
            while True:
                index = review_upper.find(word_upper, start)
                if index == -1:
                    break
                review = review[:index] + "*" * len(word) + review[index + len(word):]
                review_upper = review.upper()  # actualizamos para que coincida
                start = index + len(word)
    return review

import re # Importo la funcion re, para analizar de manera mas sencilla patrones de strings.


def validate_email(email):
    valid = True
    while valid:
        if "@" not in email:
            valid = False
        if email.startswith("@"):
            valid = False
        if not re.search(r"@.+\.", email):   # Verifica que haya un punto luego del arroba.
            valid = False
        if email.endswith("@"):
            valid = False
        if email.startswith("."):
            valid = False
        if email.endswith("."):
            valid = False
        dominio = email.split(".")[-1]
        if len(dominio) < 2:
            valid = False
        break;
    return valid