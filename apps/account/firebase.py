import firebase_admin

from environs import Env
from firebase_admin import credentials, auth

env = Env()
env.read_env()


# cred = credentials.Certificate(env.str('CERTIFICATE_TO_FIREBASE_JSON'))  # Firebase credentials certificate
# firebase_admin.initialize_app(cred)


def check_token(id_token):
    user = auth.verify_id_token(id_token)
    return user
