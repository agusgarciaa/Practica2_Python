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


def calculate_cost(weight, zone):
    weight = float(weight)
    if (weight > 0) and (weight <= 1.0):
        match zone:
            case "local":
                value = 500
            case "regional":
                value = 1000
            case "nacional":
                value = 2000
            case _:
                value = "Zona no válida. Las zonas disponibles son: local, regional, nacional. "
    elif (weight > 1.0) and (weight <= 5.0):
        match zone:
            case "local":
                value = 1000
            case "regional":
                value = 2500
            case "nacional":
                value = 4500
            case _:
                value = "Zona no válida. Las zonas disponibles son: local, regional, nacional. "
    elif weight > 5.0:
        match zone:
            case "local":
                value = 2000
            case "regional":
                value = 5000
            case "nacional":
                value = 8000
            case _:
                value = "Zona no válida. Las zonas disponibles son: local, regional, nacional. "
    else:
        return "Peso no válido."
    return value


def all_hashtags(posts):
    hashtags = {}
    
    for post in posts:
        words = post.split()
        
        for word in words:
            if word.startswith("#"):

                if word in hashtags:
                    hashtags[word] += 1
                else:
                    hashtags[word] = 1
    return hashtags


def trending_hashtags(hashtags):
    in_order = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    print("Hashtags trending (más de una aparición): ")
    for tag, cant in in_order:
        if cant > 1:
            print(f"{tag}: {cant}")
    return


def cipher(positions, message):
    encrypted = ""

    for letter in message:
        if letter.isalpha():
            new = chr(ord(letter) + positions) #ord() convierte una letra a número y chr() viceversa
            encrypted += new
        else:
            new = letter
            encrypted += new
    return encrypted


def decipher(positions, encrypted):
    message = ""

    for letter in encrypted:
        if letter.isalpha():
            new = chr(ord(letter) - positions)
            message += new
        else:
            new = letter
            message += new
    return message


def clean_name(name):
    if not name or name.strip() == "":
        return None
    return name.strip().title()


def clean_grade(grade):
    if grade and grade.isdigit():
        return int(grade)
    else:
        return None


def clean_status(status):
    if not status:
        return None
    return status.strip().title()


def clean_everything(students):
    new_students = []

    for student in students:
        name = clean_name(student["name"])
        grade = clean_grade(student["grade"])
        status = clean_status(student["status"])

        if name:
            if grade:
                new_students.append({
                    "name": name,
                    "grade": grade,
                    "status": status
                })
    return new_students


def no_more_duplicates(students):
    uniques = {}

    for student in students:
        name = student["name"]
        grade = student["grade"]

        if name not in uniques:
            uniques[name] = student
        else:
            current = grade
            existing = uniques[name]["grade"]

            if current is not None:
                if existing is None or current > existing:
                    uniques[name] = student

    return list(uniques.values())

    
def total_scores(totals, participant, score):
    if participant not in totals:
        totals[participant] = score
    else:
        totals[participant] += score
    return totals


def update_winners(wins, winner):
    if winner not in wins:
        wins[winner] = 1
    else:
        wins[winner] += 1
    return wins


def check_round(rounds):
    i = 1
    wins = {}
    totals = {}
    best = {}
    
    for round_data in rounds:
        print(f"\nRonda {i} - {round_data["theme"]}")
        round_scores = {}
        
        for participant, scores in round_data["scores"].items():
            total = sum(scores.values())
            round_scores[participant] = total
            
            if participant not in best:
                best[participant] = total
            else:
                if best[participant] < total:
                    best[participant] = total
                    
            totals = total_scores(totals, participant, total)
            
        ranking = sorted(round_scores.items(), key=lambda x: x[1], reverse=True)
        winner, score_winner = ranking[0]
        wins = update_winners(wins,winner)
        print(f"Ganador: {winner} ({score_winner} pts.)")
        
        for participant, score in ranking[1:]:
            print(f"{participant}: {score} pts")    
        i += 1
    return wins, totals, best
        

def show_final_table(wins, totals, best, rounds):
    print("------------------------------"*3 + "\nTabla de posiciones final: \nCocinero       | Puntaje      | Rondas Ganadas  | Mejor Ronda  | Promedio")
    print("------------------------------"*3)
    final_scores = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    
    for participant, score in final_scores:
        average = (score/rounds)
        print(f"{participant}      | {score}    | {wins.get(participant, 0)}    | {best[participant]}    | {average}")

    print("------------------------------"*3)
    return
        
        