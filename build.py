"""Скрипт локальной сборки СпортТовары: python build.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def check_python_version():
    print(f'[1/5] Python {sys.version.split()[0]}')
    if sys.version_info < (3, 10):
        print('Требуется Python 3.10+')
        sys.exit(1)


def install_dependencies():
    req = os.path.join(ROOT, 'requirements.txt')
    if os.path.exists(req):
        print('[2/5] Установка зависимостей')
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', req], check=True)
    else:
        print('[2/5] Внешних зависимостей нет (только стандартная библиотека)')


def check_data():
    print('[3/5] Проверка data/products.json')
    if not os.path.exists(os.path.join(ROOT, 'data', 'products.json')):
        print('Файл данных не найден!')
        sys.exit(1)


def run_tests():
    print('[4/5] Запуск тестов')
    result = subprocess.run(
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests'],
        capture_output=True, text=True, cwd=ROOT
    )
    print('\n'.join(result.stderr.strip().splitlines()[-3:]))
    if result.returncode != 0:
        print(result.stdout, result.stderr)
        print('Тесты не прошли!')
        sys.exit(1)


def run_app():
    print('[5/5] Запуск приложения (демо-сценарий)')
    result = subprocess.run([sys.executable, 'main.py', '--demo'], capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print(result.stderr)
        print('Приложение завершилось с ошибкой!')
        sys.exit(1)
    print('\n'.join(result.stdout.splitlines()[-5:]))


if __name__ == '__main__':
    check_python_version()
    install_dependencies()
    check_data()
    run_tests()
    run_app()
    print('Сборка успешна!')
