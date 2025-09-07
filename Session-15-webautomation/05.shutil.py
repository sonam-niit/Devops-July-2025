import shutil

# simple copy the file
# shutil.copy("file.txt","copy_file.txt")
# copy with meta data
# like permission timestamps
# shutil.copy2("file.txt","copy_file.txt")
print("file copied successfully")

# copy entire directory
# shutil.copytree("my_folder","backup_folder")

shutil.make_archive("project","zip","project_folder")
# creating zip archive

#extract archive
shutil.unpack_archive("project.zip","restored project")

