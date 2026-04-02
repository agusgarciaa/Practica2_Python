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
        