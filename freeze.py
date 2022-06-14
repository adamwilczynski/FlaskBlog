from pathlib import Path

from flask_frozen import Freezer

from blog import app

freezer = Freezer(app)
# app.config["FREEZER_BASE_URL"] = "entropista.tech"
app.config["FREEZER_DESTINATION"] = "docs"
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True

if __name__ == "__main__":
    freezer.freeze()

    # for file_name in ("about", "contact", "post"):
    #     p = Path(f"./docs/{file_name}")
        # with open(p, encoding="UTF-8") as f:
        #     fixed_relative_path = f.read().replace(
        #         "../static",
        #         "./static",
        #     )
        #     with open(p, "w", encoding="UTF-8") as f:
        #         f.write(fixed_relative_path)
        # p.rename(p.with_suffix(".html"))
