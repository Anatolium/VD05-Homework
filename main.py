from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def poem():
#     context = {
#         "caption": "Французские фильмы",
#         "link": "Посмотреть фильм",
#         "user": "Анатолий",
#         "number": 8,
#         "list": ["Nina", "Karina", "Anton", "Nikita"],
#         "poem": [
#             "Сижу за решёткой в темнице сырой.",
#             "Вскормленный в неволе орёл молодой,",
#             "Мой грустный товарищ, махая крылом,",
#             "Кровавую пищу клюёт под окном,",
#             "Клюёт, и бросает, и смотрит в окно,",
#             "Как будто со мною задумал одно."]
#     }
#     return render_template("shablon.html", **context)

# Код урока из shablon.html
# <!--<body>-->
# <!--{% if user %}-->
# <!--<p>Вы вошли под именем {{user}}</p>-->
# <!--{% endif %}-->
# <!--<p>Вы должны выложить {{number}}-->
# <!--    {% if number == 1 %}-->
# <!--    пост-->
# <!--    {% elif 2 <= number <= 4 %}-->
# <!--    поста-->
# <!--    {% else %}-->
# <!--    постов-->
# <!--    {% endif %}-->
# <!--</p>-->
# <!--<p>-->
# <!--    {% for user in list %}-->
# <!--    {{user}}-->
# <!--    {% endfor %}-->
# <!--</p>-->
# <!--<h1>Стихотворение Пушкина</h1>-->
# <!--<p>-->
# <!--    {% for i in poem %}-->
# <!--    {{i}}<br>-->
# <!--    {% endfor %}-->
# <!--</p>-->

@app.route("/")
def films():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("index.html", **context)


@app.route("/person/")
def person():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("main.html", **context)


if __name__ == "__main__":
    app.run()
