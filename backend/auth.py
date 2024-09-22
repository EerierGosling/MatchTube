from propelauth_py import init_base_auth, UnauthorizedException
import os
import dotenv

dotenv.load_dotenv()

# Get the auth url and api key from the environment variables
PROPELAUTH_AUTH_URL = os.getenv("PROPELAUTH_AUTH_URL")
PROPELAUTH_API_KEY = os.getenv("PROPELAUTH_API_KEY")

auth = init_base_auth(PROPELAUTH_AUTH_URL, PROPELAUTH_API_KEY)

auth_header = None # get authorization header sent from the frontend in the form `Bearer {TOKEN}`
try:
    user = auth.validate_access_token_and_get_user(auth_header)
    print("Logged in as", user.user_id)
except UnauthorizedException:
    print("Invalid access token")

