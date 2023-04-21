import os

from dotenv import load_dotenv
load_dotenv()


BASE_URL = os.getenv('BASE_URL')
USER = {
        'login': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
}

DEVICE = os.getenv('DEVICE')

BROWSER_OPTIONS = {
        'geolocation': {
                'latitude': float(os.getenv('LATITUDE')),
                'longitude': float(os.getenv('LONGITUDE'))
        },
        'permissions': ['geolocation']
}

