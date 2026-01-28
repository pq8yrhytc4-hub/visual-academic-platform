SECTIONS = [
    "pathology","etiology","physiopathology","symptoms","signs",
    "clinical features","diagnosis","investigations","treatment",
    "pharmacology","surgical treatment","complications",
    "prevention","control","transmission"
]

def split_sections(text):
    result = {s: "" for s in SECTIONS}
    current = None
    for line in text.splitlines():
        l = line.lower().strip()
        for s in SECTIONS:
            if s in l:
                current = s
        if current:
            result[current] += line + "\n"
    return result
