import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Others": []
}

def organize_files(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            print("The specified directory does not exist.")
            return
        
        # Loop through all files in the directory
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            # Find the file extension
            _, file_extension = os.path.splitext(file)
            
            # Find the category for the file
            folder_name = "Others"
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension.lower() in extensions:
                    folder_name = category
                    break
            
            # Create the category folder if it doesn't exist
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Move the file to the respective folder
            shutil.move(file_path, os.path.join(folder_path, file))
        
        print("Files have been organized successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dir_path = input("Enter the path of the directory to organize: ")
    organize_files(dir_path)
