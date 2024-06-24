# Проект "FlaskWorldITDiplom"

## Перечень участников

- [Науменко Никита]()
- [Олефиренко Глеб]()
- [Лесковец Кирилл]()
- [Мартыненко Святослав]()

## Описание Flask приложений

### Приложение home_page: 

#### Установка и запуск
1. Клонируйте репозиторий: `git clone https://github.com/yourrepo`
2. Перейдите в директорию проекта: `cd yourrepo`
3. Установите зависимости: `pip install -r requirements.txt`
4. Запустите приложение: `flask run`

#### Примеры использования
- Создание поста: Перейдите на `/create_post` и заполните форму.
- Просмотр постов: Перейдите на `/posts`.

### Приложение 2: Книга рецептов
Приложение для хранения и поиска кулинарных рецептов.

#### Установка и запуск
1. Клонируйте репозиторий: `git clone https://github.com/yourrepo`
2. Перейдите в директорию проекта: `cd yourrepo`
3. Установите зависимости: `pip install -r requirements.txt`
4. Запустите приложение: `flask run`

#### Примеры использования
- Добавление рецепта: Перейдите на `/add_recipe` и заполните форму.
- Поиск рецептов: Перейдите на `/search`.

## Описание Flask моделей

### Модель 1: Пользователь
Описание модели пользователя, её поля и методы.

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
