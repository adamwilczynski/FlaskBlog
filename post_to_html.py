import markdown

with open("posts/Creating and publishing a Flask Blog Part I.md", "r", encoding="utf-8") as f:
    text = f.read()
html = markdown.markdown(text, extensions=['codehilite', 'fenced_code'])
