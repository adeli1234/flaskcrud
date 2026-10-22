from app import app
from app.contacts import contacts

app.register_blueprint(contacts)

# starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
