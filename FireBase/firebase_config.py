import pyrebase

class FirebaseConfig:
    CONFIG = {
        "apiKey": "AIzaSyChX3dYojSJAh5cQGuTw8rdBdGdcT23zlE",
        "authDomain": "hoteles-pqt.firebaseapp.com",
        "databaseURL": "https://hoteles-pqt-default-rtdb.europe-west1.firebasedatabase.app/",
        "projectId": "hoteles-pqt",
        "storageBucket": "hoteles-pqt.firebasestorage.app",
        "messagingSenderId": "134584152529",
        "appId": "1:134584152529:web:df6ef55ec18c813e70f0f0",
        "measurementId": "G-LHMZGQ1XRE"
    }

    @classmethod
    def initialize(cls):
        firebase = pyrebase.initialize_app(cls.CONFIG)
        return firebase.auth()

auth = FirebaseConfig.initialize()
