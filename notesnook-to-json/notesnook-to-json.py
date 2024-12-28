import sys, os, shutil, pathlib, json

if len(sys.argv) != 3:
    print("Error: Expected exactly two arguments (input file and output file).")
    exit(1)

INPUT_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

EXTRACT_PATH = "extracted"
if os.path.exists(EXTRACT_PATH):
    print(f"Error: There can't be a file or directory called \"{EXTRACT_PATH}\" in the current directory. Please rename or remove it.")
    exit(1)

shutil.unpack_archive(INPUT_PATH, EXTRACT_PATH)

def extract_title(filecontent: str) -> str:
    return filecontent.split("\n", 1)[0]

def extract_content(filecontent: str) -> str:
    delimiter = "\n\n  "
    start = filecontent.index(delimiter) + len(delimiter)
    return filecontent[start:].strip()

notes = []
for file in pathlib.Path(EXTRACT_PATH).iterdir():
    if file.is_dir():
        print(f'ignoring notebook "{file.name}"...')
        continue

    filecontent = file.read_text()
    notes.append({
        "title": extract_title(filecontent),
        "content": extract_content(filecontent)
    })

shutil.rmtree(EXTRACT_PATH)

# case sensitive sort
notes.sort(key=lambda note: note["title"])

with open(OUTPUT_PATH, "w") as output:
    # ensure_ascii=False to avoid \uHHHH characters, e.g. for emojis
    json.dump(notes, output, indent=4, ensure_ascii=False)

print(f"processed {len(notes)} notes.")