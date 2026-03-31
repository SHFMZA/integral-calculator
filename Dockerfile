FROM python:3.10-slim

# Установка Tkinter и системных зависимостей для GUI
RUN apt-get update && apt-get install -y \
    tk \
    python3-tk \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копирование файлов
COPY integral_calculator.py .
COPY requirements.txt .

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск программы
CMD ["python3", "integral_calculator.py"]