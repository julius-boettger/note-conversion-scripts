# JSON to Notesnook
> also see [notesnook-to-json](https://github.com/julius-boettger/notesnook-to-json)

Takes a JSON file containing your notes like
```json
[
    {
        "title": "Title of the note",
        "content": "Content of the note"
    },
    ...
]
```
as the input and outputs a bunch of `.txt` files that can be imported into Notesnook (as plain text notes).

## Prerequisites
- `python` is installed / accessible

## Installation
```sh
git clone https://github.com/julius-boettger/note-conversion-scripts
cd note-conversion-scripts/json-to-notesnook
```

## Usage
### Step 1: Run the script
```sh
# general usage:
python json-to-notesnook.py [input_json_file_path] [output_directory_path]
# for example...
python json-to-notesnook.py notes.json export
```

### Step 2: Use the [Notesnook Importer](https://importer.notesnook.com/)
- Open the [Notesnook Importer](https://importer.notesnook.com/)
- Select "Text" as the notes app
- Click to select files
- Select all the `.txt` files the script generated
- "Start processing"
- "Download ZIP file" should result in a `notesnook-importer.zip`

### Step 3: Import into Notesnook
- e.g. in [Notesnook Web](https://app.notesnook.com):
    - Go to "Settings", "Notesnook Importer"
    - Upload your `notesnook-importer.zip`
    - "Start import"