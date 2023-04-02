def contamination(text, char):
    if len(text) >= 1:
        return char * len(text)
    else:
        return ''

print(contamination("_3ebzgh4","&"))