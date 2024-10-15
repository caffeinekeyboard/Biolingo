import os
import zipfile
def unzip_files_in_folder(zip_folder_path, extract_folder_path):
    os.makedirs(extract_folder_path, exist_ok=True)
    for filename in os.listdir(zip_folder_path):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(zip_folder_path, filename)
            # Open the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all contents to the target folder
                zip_ref.extractall(extract_folder_path)
            print(f"Extracted: {filename}")

zip_folder_path = '/home/aarya/Desktop/Biolingo/zipped_data'
extract_folder_path = '/home/aarya/Desktop/Biolingo/data/all_videos'
unzip_files_in_folder(zip_folder_path, extract_folder_path)
