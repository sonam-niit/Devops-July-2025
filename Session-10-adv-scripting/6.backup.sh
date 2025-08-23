SOURCE_DIR=/home/sonam/developers

BACKUP_DIR=myapp
LOG_FILE="app.log"

mkdir -p "$BACKUP_DIR"

## Create Compressed file
tar -czf "$BACKUP_DIR/$LOG_FILE" -C "$SOURCE_DIR" .

