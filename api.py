from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os # Γιατι δεν θα γίνει από ένα μόνο os το development

#Εισαγωγή των παρμέτρων από το αρχείο .env
load_dotenv()

#Δημιουργία Flash app
app = Flask(__name__)

#Σύνδεση με την βάση δεδομένων
mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017/")
client= MongoClient(mongo_uri)
db= client["unipishop"]

# Μεταρτροπή του ObjectId σε string
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

#Δημιουργία test endpoint
@app.route('/api/test', methods=['GET'])
def ping():
    return jsonify({"message": "API is working!"})

#Επιστροφή όλων των προϊόντων με μέθοδο GET
@app.route('/api/products', methods=['GET'])
def get_products():
    products = db.products.find()
    serialized =[serialize_doc(p) for p in products]
    return jsonify(serialized)



#Εκκίνηση του app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)