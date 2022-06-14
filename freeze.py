from flask_frozen import Freezer

from blog import app

freezer = Freezer(app)
# app.config["FREEZER_BASE_URL"] = "entropista.tech"
app.config["FREEZER_DESTINATION"] = "docs"

if __name__ == "__main__":
    freezer.freeze()