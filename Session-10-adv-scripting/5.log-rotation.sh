#!/bin/bash
LOG_DIR="myapp"
LOG_FILE="app.log"
MAX_BACKUPS=3

##Log Rotation
#Example app.log.1.gz --> becomes app.log.2.gz
for (( i=$MAX_BACKUPS; i>0; i--)); do
    if [ -f "$LOG_DIR/$LOG_FILE.$i.gz" ]; then
        next=$((i+1))
        mv "$LOG_DIR/$LOG_FILE.$i.gz" "$LOG_DIR/$LOG_FILE.$next.gz"
    fi
done

## Let's Compress
if [ -f "$LOG_DIR/$LOG_FILE" ]; then 
    mv "$LOG_DIR/$LOG_FILE" "$LOG_DIR/$LOG_FILE.1"
    gzip "$LOG_DIR/$LOG_FILE.1"
fi

#incase no files then create fresh empty log file
touch "$LOG_DIR/$LOG_FILE"

## Delete logs beyonds limit
if [ -f "$LOG_DIR/$LOG_FILE.$((MAX_BACKUPS+1)).gz" ]; then
    rm "$LOG_DIR/$LOG_FILE.$((MAX_BACKUPS+1)).gz"
fi