from flask import Flask
from backend.routes import init_routes  # Import your routes

app = Flask(__name__)

# Any config settings or environment variables can be set here
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
