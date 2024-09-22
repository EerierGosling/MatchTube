from flask import Flask
from routes import init_routes  # Import your routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://matchtube.xyz"}})

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
