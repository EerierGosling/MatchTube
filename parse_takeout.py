import re

def get_video_ids(input_file):
    with open(input_file, 'r') as file:
        input_file = file.read()

    # Define the regex pattern to match YouTube video IDs
    pattern = r"https://www\.youtube\.com/watch\?v=([^&\"'<>]+)"
    matches = re.findall(pattern, input_file)

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