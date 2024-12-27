import sys, pathlib, json

if len(sys.argv) != 3:
    print("Error: Expected exactly two arguments (input file and output directory).")
    exit(1)

INPUT_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

output_path = pathlib.Path(OUTPUT_PATH)
output_path.mkdir(parents=True, exist_ok=True)

with open(INPUT_PATH, "r") as input_file:
    notes = json.load(input_file)

for note in notes:
    note_path = output_path / (note["title"] + ".txt")
    with open(note_path, "w") as note_file:
        note_file.write(note["content"])