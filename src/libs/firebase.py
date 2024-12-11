import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("freshify-c85ea-firebase-adminsdk-5wykt-97e18b0ec2.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def create_checkout_to_firebase(data):
    
    data_to_firebase = {
        "id": data['id'][0],
        "email": data['email'][0],
        "items": data['items'][0],
        "total_price": data['total_price'][0],
        "address": data['address'][0],
        "payment": data['payment'][0],
        "status": data['status'][0]
    }
    db.collection('checkout').add(document_data=data_to_firebase)