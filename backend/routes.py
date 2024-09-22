from flask import request, jsonify, send_from_directory
from propelauth_py import init_base_auth
import dotenv
import os
import requests

from get_video_data import get_video_data
from parse_takeout import get_video_ids
from atlas_vector import upload_user_data, find_closest_user

dotenv.load_dotenv()

auth = init_base_auth(
    os.getenv("PROPELAUTH_AUTH_URL"),
    os.getenv("PROPELAUTH_API_KEY"),
)

# Initialize routes with the Flask app
def init_routes(app):

    # Route for file uploads
    @app.route('/takeout', methods=['POST'])
    def upload_file():

        file = request.files.get('file')
        email = request.form.get('email')

        if not file or not email:
            return jsonify({'message': 'no email or no file'}), 400
        
        # Check if the file has a name
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        # Pass the file to the processing function
        upload_user_data(email, get_video_data(get_video_ids(file)))

        # Respond with the result of the file processing
        return jsonify({'message': 'File successfully processed!'}), 200
    
    @app.route('/user/<string:user_id>', methods=['GET'])
    def get_user_data(user_id):
        # Here, you can add logic to retrieve user data based on user_id
        print(f"Received request for user ID: {user_id}")

        return jsonify({'closest_user': find_closest_user(user_id)}), 200
    
    @app.route('/user-info/<string:email>', methods=['GET'])
    def get_user_info_by_email(email):

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        # URL for fetching user details by email
        user_info_url = f"{os.getenv('PROPELAUTH_AUTH_URL')}/api/backend/v1/user/email?email={email}&include_orgs=true"

        # Send request to PropelAuth API to fetch user data
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv("PROPELAUTH_API_KEY")}',
        }
        response = requests.get(user_info_url, headers=headers)

        if response.status_code != 200:
            return jsonify({'error': 'User not found'}), response.status_code

        user_data = response.json()

        # Extracting relevant data: name and profile picture URL
        return jsonify({
            'name': f"{user_data.get('first_name')} {user_data.get('last_name')}",
            'profile_picture_url': user_data.get('picture_url')
        }), 200


