from flask import request, jsonify

from get_video_data import get_video_data
from parse_takeout import get_video_ids
from atlas_vector import upload_user_data

# Initialize routes with the Flask app
def init_routes(app):

    # Route for file uploads
    @app.route('/upload', methods=['POST'])
    def upload_file():

        print(request.form)

        print("got post")

        file = request.files.get('file')
        email = request.form.get('email')

        print(email)

        if not file or not email:
            return jsonify({'message': 'no email or no file'}), 400

        print("got stuff")
        
        # Check if the file has a name
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400
        
        print("got filename")

        # Pass the file to the processing function
        process_file(file, email)

        # Respond with the result of the file processing
        return jsonify({'message': 'File successfully processed!'}), 200

# Function to process the uploaded file (in-memory)
def process_file(file, email):
    """
    This function processes the uploaded file without saving it to disk.
    The 'file' parameter is a file object that can be read directly.
    """

    upload_user_data(email, get_video_data(get_video_ids(file)))
