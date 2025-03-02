import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Executables": [".exe", ".bat", ".sh"],
}

# Set the directory to organize
DIRECTORY = "C:/Users/YourUsername/Downloads"  # Change this to your target directory

def organize_files():
    """Organizes files into categorized folders based on extensions."""
    if not os.path.exists(DIRECTORY):
        print("Directory not found!")
        return

    for filename in os.listdir(DIRECTORY):
        file_path = os.path.join(DIRECTORY, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Find the appropriate category
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_path = os.path.join(DIRECTORY, category)
                    os.makedirs(category_path, exist_ok=True)  # Create category folder if not exists
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved: {filename} → {category}/")
                    break  # Stop checking once a category is found

if __name__ == "__main__":
    organize_files()
