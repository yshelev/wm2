# logs Parser
## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)

## Технологии
Парсинг данных производился с помощью встроенной в python библиотеки argparse, создание тестов с помощью библиотеки pytest

## Использование
1. Склонируйте репозиторий:
   ```sh
   git clone https://github.com/yshelev/wm2.git
   cd workmate
   ```
2. Создайте и активируйте виртуальное окружение: 
   ```sh
   python3 -m venv .venv
   .venv/Scripts/activate
   ```
3. Установите необходимые зависимости:  	
   ```sh
   pip install -r requirements.txt
   ```
4. В директорию data/csv поместите csv файлы (допустимые разрешения: *.csv)
5. Запустите программу:
   ```sh
   python main.py [paths to files] --report [report name] 
   ```
Пример работы программы:
![image](https://github.com/user-attachments/assets/83f66088-981f-44c1-9a27-4d17f4949fbb)

Для запуска тестов: 
1. Перейдите в директорию tests:
   ```sh
     cd tests
   ```
2. Запустите тесты:
   ```sh
     pytest .
   ```
3. Для получения процента покрытия кода тестами:
   ```sh
     pytest --cov
   ```

## Команда проекта

- [Шелевой Ярослав](https://github.com/yshelev) — Backend developer
