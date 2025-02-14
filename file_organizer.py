import os
import shutil
import logging
from tkinter import Tk, filedialog, messagebox

# Setup logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO)

def load_categories():
    return {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

def organize_files(directory):
    categories = load_categories()
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1]
            moved = False
            for category, extensions in categories.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, category)
                    os.makedirs(folder_path, exist_ok=True)
                    try:
                        shutil.move(file_path, os.path.join(folder_path, file))
                        logging.info(f"Moved: {file} to {folder_path}")
                        moved = True
                        break
                    except Exception as e:
                        logging.error(f"Error moving {file}: {e}")
                        break
            if not moved:
                others_path = os.path.join(directory, "Others")
                os.makedirs(others_path, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(others_path, file))
                    logging.info(f"Moved: {file} to {others_path}")
                except Exception as e:
                    logging.error(f"Error moving {file}: {e}")

def select_directory():
    path = filedialog.askdirectory()
    if path:
        organize_files(path)
        messagebox.showinfo("Success", "Files organized successfully!")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    select_directory()