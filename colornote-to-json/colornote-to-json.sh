#!/bin/sh

if [ $# -ne 2 ]; then
  echo "Error: Expected exactly two arguments (input file and output file)."
  exit 1
fi

input=$1
output=$2
decryptor_path=ColorNote-backup-decryptor

read -s -p "Enter ColorNote master password: " password
printf "\nAttempting decrypt...\n"

java -cp $decryptor_path/lib/bcprov-jdk15on-154.jar:$decryptor_path/lib/bcpkix-jdk15on-154.jar:$decryptor_path/bin ColorNoteBackupDecrypt $password 28 \
    < $input \
    | $decryptor_path/fixup-v2 \
    | tail -n +2 \
    | jq -s '[ .[] | {title, content: .note} ]' \
    > $output

if [ $? == 0 ]; then
  echo "Success! Wrote to $output"
fi