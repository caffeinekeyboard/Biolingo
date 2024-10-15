import os
import zipfile

def unzip_files_in_folder(zip_folder_path, extract_folder_path):
    # Loop through all files in the zip folder
    for filename in os.listdir(zip_folder_path):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(zip_folder_path, filename)
            # Create a folder for the contents of this zip file
            folder_name = os.path.splitext(filename)[0]
            extract_to = os.path.join(extract_folder_path, folder_name)
            os.makedirs(extract_to, exist_ok=True)
            
            # Open the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract contents into the dedicated folder
                zip_ref.extractall(extract_to)
            print(f"Extracted {filename} to {extract_to}")

# Example usage
zip_folder_path = '/home/aarya/Desktop/Biolingo/zipped_data'
extract_folder_path = '/home/aarya/Desktop/Biolingo/data/seperated'
unzip_files_in_folder(zip_folder_path, extract_folder_path)
