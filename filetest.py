file_path = "example.txt"  # Path of the text file to be created

# Open the file in write mode and create it if it doesn't exist
with open(file_path, "w") as file:
    file.write("This is some example text.\n")
    file.write("Writing to a text file in Python.\n")
    file.write("It's easy to do!\n")

print("Text file created and written successfully.")
