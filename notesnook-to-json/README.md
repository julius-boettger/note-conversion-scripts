# Notesnook to JSON

Takes a `.zip` of your exported Notesnook notes as the input and outputs a JSON file containing all your notes like
```json
[
    {
        "title": "Title of the note",
        "content": "Content of the note"
    },
    ...
]
```

## Prerequisites
- `python` is installed / accessible

## Installation
```sh
git clone https://github.com/julius-boettger/note-conversion-scripts
cd note-conversion-scripts/notesnook-to-json
```

## Usage
### Acquiring your Notesnook `.zip`
- Export all notes from Notesnook as plain text, e.g. from [Notesnook Web](https://app.notesnook.com):
    - Go to "Settings", "Backup & export", "Export all notes"
    - Select format "Text"
    - Enter your password

### Running the script with your Notesnook `.zip`
```sh
# general usage:
python notesnook-to-json.py [input_zip_file_path] [output_json_file_path]
# for example...
python notesnook-to-json.py notes.zip notes.json
```
