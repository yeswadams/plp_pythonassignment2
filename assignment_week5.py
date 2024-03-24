try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("Line 2: 12345\n")
        file.write("Another line with text\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Content of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 4\n")
        file.write("Line 5: 67890\n")
        file.write("Final line\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Task completed.")

