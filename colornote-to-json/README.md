# ColorNote to JSON
### A minimalistic wrapper for [ColorNote backup decryptor](https://github.com/olejorgenb/ColorNote-backup-decryptor)

Takes an encrypted ColorNote backup file as the input and outputs a JSON file containing all your notes like
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
- `java` and `jq` are installed / accessible
- a Unix-like operating system (WSL / Cygwin should also work)

## Installation
```sh
git clone --recurse-submodules https://github.com/julius-boettger/note-conversion-scripts
cd note-conversion-scripts/colornote-to-json
```

## Usage
### Acquiring the ColorNote backup file
- Create a manual backup in ColorNote
    - Go to "Settings", "Backup", "Backup Notes"
    - Enter your password (you will need it again later!)
- Transfer the backup file to the device you want to run this script on
    - e.g. tap on the Backup and select "Send", followed by a service of your choice

### Running the script with your ColorNote backup file
```sh
# general usage:
./colornote-to-json.sh [input_backup_file_path] [output_json_file_path]
# for example...
./colornote-to-json.sh colornote-20240424.backup notes.json
```