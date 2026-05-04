from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import User


def init_routes(app):

    @app.route('/users', methods=['GET', 'POST'])
    def users():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']

            if User.query.filter_by(username=username).first():
                flash('Пользователь уже существует')
                return redirect(url_for('users'))

            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            flash('Пользователь успешно добавлен!')
            return redirect(url_for('users'))

        search = request.args.get('search')

        if search:
            users = User.query.filter(User.username.contains(search)).all()
        else:
            users = User.query.all()

        return render_template('users.html', users=users)


    @app.route('/delete/<int:id>')
    def delete_user(id):
        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()
        flash('Пользователь удален!')
        return redirect(url_for('users'))


    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit_user(id):
        user = User.query.get_or_404(id)

        if request.method == 'POST':
            user.username = request.form['username']
            user.email = request.form['email']

            db.session.commit()
            flash('Данные пользователя обновлены!')
            return redirect(url_for('users'))

        return render_template('edit_user.html', user=user)


    # ========== ГЛАВНАЯ СТРАНИЦА ==========
    @app.route('/')
    @app.route('/index')
    def index():
        user = {'username': 'Гость'}
        return render_template('index.html', title='Главная', user=user)


    # ========== ВХОД (с поддержкой POST) ==========
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            flash(f'Добро пожаловать, {username}!')
            return redirect(url_for('index'))
        return render_template('login.html', title='Вход')


    # ========== ЗАДАНИЕ 1: Список студентов ==========
    @app.route('/students')
    def students():
        students_list = [
            {'name': 'Анна Иванова', 'age': 20, 'grade': 85},
            {'name': 'Пётр Петров', 'age': 22, 'grade': 58},
            {'name': 'Мария Сидорова', 'age': 19, 'grade': 92},
            {'name': 'Иван Козлов', 'age': 21, 'grade': 45},
            {'name': 'Елена Смирнова', 'age': 20, 'grade': 74},
            {'name': 'Дмитрий Новиков', 'age': 23, 'grade': 67},
        ]
        
        threshold = request.args.get('threshold', 60, type=int)
        
        return render_template('students.html', students=students_list, threshold=threshold)


    # ========== ЗАДАНИЕ 2: Каталог товаров ==========
    @app.route('/products')
    def products():
        products_list = [
            {'name': 'Ноутбук Apple MacBook Pro', 'price': 180000, 'in_stock': True},
            {'name': 'Мышь Logitech MX Master', 'price': 8500, 'in_stock': False},
            {'name': 'Монитор Dell 27"', 'price': 35000, 'in_stock': True},
            {'name': 'Клавиатура Mechanical', 'price': 12000, 'in_stock': True},
            {'name': 'Наушники Sony WH-1000XM5', 'price': 30000, 'in_stock': False},
            {'name': 'USB-хаб', 'price': 1500, 'in_stock': True},
            {'name': 'Смартфон Samsung Galaxy', 'price': 70000, 'in_stock': True},
            {'name': 'Внешний SSD 1TB', 'price': 11000, 'in_stock': True}
        ]
        
        price_threshold = request.args.get('price_threshold', 20000, type=int)
        
        return render_template('products.html', 
                             products=products_list, 
                             price_threshold=price_threshold)


    # ========== ЗАДАНИЕ 3: Новости сайта ==========
    @app.route('/news')
    def news():
        leader_articles = [
            {
                'id': 1,
                'title': 'Будущее искусственного интеллекта в 2025 году',
                'tags': ['AI', 'Технологии', 'Будущее'],
                'content_preview': 'Искусственный интеллект продолжает развиваться невероятными темпами. Узнайте, что нас ждет в ближайшие годы...'
            },
            {
                'id': 2,
                'title': 'Новый релиз Python 3.13: что нового?',
                'tags': ['Python', 'Программирование'],
                'content_preview': 'Разработчики представили долгожданное обновление языка Python с улучшенной производительностью...'
            },
            {
                'id': 3,
                'title': 'Flask 3.0: революция в веб-разработке',
                'tags': ['Flask', 'Web', 'Python'],
                'content_preview': 'Новая версия популярного фреймворка приносит множество улучшений...'
            }
        ]
        
        hot_news = [
            {'title': '🔥 Скидки 50% на всю электронику!', 'short_description': 'Только до конца недели. Успейте купить!'},
            {'title': '🔥 Анонс Flask 3.0', 'short_description': 'Новые возможности и улучшения производительности'},
            {'title': '🔥 Бесплатный вебинар по Python', 'short_description': 'Регистрация открыта на сайте'}
        ]
        
        regular_news = [
            {'title': 'Открытие нового парка в центре города', 'short_description': 'В выходные состоится торжественное открытие'},
            {'title': 'Конкурс фото: главный приз 50 000 руб', 'short_description': 'Принимаются работы на тему "Город будущего"'},
            {'title': 'Новая выставка в музее современного искусства', 'short_description': 'Работы молодых художников со всей страны'}
        ]
        
        qa_items = [
            {'question': 'Как зарегистрироваться на сайте?', 'answer': 'Нажмите на кнопку "Вход" и заполните форму'},
            {'question': 'Где посмотреть список студентов?', 'answer': 'Перейдите по ссылке "Студенты" в меню навигации'},
            {'question': 'Как добавить товар в корзину?', 'answer': 'Функция корзины находится в разработке'},
            {"question": "Как изменить порог сдачи?", "answer": "Откройте страницу «Студенты» и в адресной строке браузера после /students допишите ?threshold=70, где 70 — нужный вам проходной балл. Нажмите Enter."},
        ]
        
        return render_template('news.html', 
                             leader_articles=leader_articles,
                             hot_news=hot_news,
                             regular_news=regular_news,
                             qa_items=qa_items)


    # ========== ЗАДАНИЕ 4: Репозитории GitHub ==========
    @app.route('/repos')
    def repos():
        repos_list = [
            {'name': 'flask', 'language': 'Python', 'stars': 68000},
            {'name': 'react', 'language': 'JavaScript', 'stars': 220000},
            {'name': 'vue', 'language': 'JavaScript', 'stars': 50000},
            {'name': 'django', 'language': 'Python', 'stars': 75000},
            {'name': 'tensorflow', 'language': 'Python', 'stars': 185000},
            {'name': 'bootstrap', 'language': 'CSS', 'stars': 168000},
            {'name': 'pytorch', 'language': 'Python', 'stars': 80000},
            {'name': 'angular', 'language': 'TypeScript', 'stars': 95000}
        ]
        
        stars_threshold = request.args.get('stars_threshold', 100000, type=int)
        
        return render_template('repos.html', 
                             repos=repos_list, 
                             stars_threshold=stars_threshold)