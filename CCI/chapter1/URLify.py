def urlify(str):
    return str.strip().replace(" ", "%20")
str = " Jon smith  "
print(urlify(str))