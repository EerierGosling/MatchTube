import re
import zipfile
import glob
import os

def get_video_ids(folder_path):

    zip_file = glob.glob(os.path.join(folder_path, '*.zip'))[0]

    target_file_suffix = '/YouTube and YouTube Music/history/watch-history.html'

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Find the target file by checking if any file ends with the target suffix
        target_file = None
        for file in zip_ref.namelist():
            if file.endswith(target_file_suffix):
                target_file = file
                break

        if not target_file:
            raise FileNotFoundError(f"File ending with {target_file_suffix} not found in the ZIP archive.")

        # Extract the content of the target file
        with zip_ref.open(target_file) as file:
            content = file.read().decode('utf-8')

    # Define the regex pattern to match YouTube video IDs
    pattern = r"https://www\.youtube\.com/watch\?v=([^&\"'<>]+)"
    matches = re.findall(pattern, content)

    # Remove duplicates while preserving order
    seen = set()
    unique_matches = []
    for match in matches:
        if match not in seen:
            unique_matches.append(match)
            seen.add(match)
    
    return unique_matches

# # Write the unique matches to the output file
# with open('video_ids.txt', 'w') as output_file:
#     for match in unique_matches:
#         output_file.write(match + '\n')

# # Print the unique matches
# print(unique_matches)