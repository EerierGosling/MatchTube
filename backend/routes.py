from flask import request, jsonify

from get_video_data import get_video_data
from parse_takeout import get_video_ids
from atlas_vector import upload_user_data, find_closest_user

# Initialize routes with the Flask app
def init_routes(app):

    # Route for file uploads
    @app.route('/takeout', methods=['POST'])
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
        upload_user_data(email, get_video_data(get_video_ids(file)))

        # Respond with the result of the file processing
        return jsonify({'message': 'File successfully processed!'}), 200
    
    @app.route('/user/<string:user_id>', methods=['GET'])
    def get_user_data(user_id):
        # Here, you can add logic to retrieve user data based on user_id
        print(f"Received request for user ID: {user_id}")

        return jsonify({'closest_user': find_closest_user(user_id)}), 200


