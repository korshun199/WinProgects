#!/bin/bash

# Переходим в твой рабочий каталог
cd /home/work/WinProjects

# 1. Создаем структуру папок (короткие названия до 8 букв)
mkdir -p src      # Исходники
mkdir -p ui       # Дизайн (Qt Designer)
mkdir -p db       # База данных
mkdir -p assets   # Иконки/картинки

# 2. Создаем виртуальное окружение, если его еще нет
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# 3. Активируем окружение и ставим пакеты
source venv/bin/activate
pip install --upgrade pip
pip install PySide6 pyserial

# 4. Создаем заготовки файлов (латиница, коротко)
touch src/main.py    # Главный файл логики
touch src/db_work.py # Работа с БД
touch ui/main.ui     # Файл интерфейса
touch README.md      # Описание

echo "Олежка, всё готово! Виртуальное окружение настроено, пакеты PySide6 и pyserial стоят."