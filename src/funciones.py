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