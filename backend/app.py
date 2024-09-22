from flask import Flask
from routes import init_routes  # Import your routes
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/takeout": {"origins": "https://matchtube.xyz/"}})

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=port)