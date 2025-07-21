from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        title =  "Домашня сторінка",
        heading = "Вітаю у моїй CMS",
        message = "Це контент, переданий з Flask до HTML шаблону."
    )

if __name__ == ('__main__'):
    app.run(debug=True)