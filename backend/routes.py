from flask import request, jsonify

from backend.get_video_data import get_video_data
from backend.parse_takeout import get_video_ids
from backend.atlas_vector import upload_user_data

# Initialize routes with the Flask app
def init_routes(app):

    # Route for file uploads
    @app.route('/upload', methods=['POST'])
    def upload_file():
        # Check if the 'file' key is in the request
        if 'file' not in request.files:
            return jsonify({'message': 'No file part in the request'}), 400

        file = request.files['file']
        
        # Check if the file has a name
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        # Pass the file to the processing function
        process_file(file)

        # Respond with the result of the file processing
        return jsonify({'message': 'File successfully processed!'}), 200

# Function to process the uploaded file (in-memory)
def process_file(file):
    """
    This function processes the uploaded file without saving it to disk.
    The 'file' parameter is a file object that can be read directly.
    """
    
    upload_user_data("test", get_video_data(get_video_ids(file)))
