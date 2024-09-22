from flask import Flask
from routes import init_routes  # Import your routes
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "https://pennapps-project.onrender.com",
            "https://matchtube.onrender.com",
            "https://matchtube.xyz"
        ]
    }
})

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))  # Default to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=port)