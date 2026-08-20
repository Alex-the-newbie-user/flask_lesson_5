from flask import Flask, render_template

courses = [
    {
        "id": 1,
        "title": "Python с нуля",
        "teacher": "Анна Смирнова",
        "lessons": 24,
        "level": "Начальный",
        "is_available": True,
        "description": "Изучим основы Python: переменные, условия, циклы, функции и работу с коллекциями."
    },
    {
        "id": 2,
        "title": "Основы Flask",
        "teacher": "Иван Петров",
        "lessons": 16,
        "level": "Средний",
        "is_available": True,
        "description": "Научимся создавать веб-приложения на Flask, работать с маршрутами и шаблонами Jinja."
    },
    {
        "id": 3,
        "title": "Backend на Django",
        "teacher": "Олег Соколов",
        "lessons": 32,
        "level": "Продвинутый",
        "is_available": False,
        "description": "Создадим полноценное backend-приложение и познакомимся с основными возможностями Django."
    }
]

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html', courses=courses)

@app.route("/course/<int:course_id>")
def course_detail_page(course_id):
    selected_course = courses[course_id]
    return render_template('course_detail.html', sel_course = selected_course)

@app.route("/about")
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)