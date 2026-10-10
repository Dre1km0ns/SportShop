# Руководство разработчика — СпортТовары

## Настройка окружения
1. Установить Python 3.10+ и Git; редактор — VS Code с расширением Python.
2. `git clone <url> SportShop && cd SportShop`
3. (Необязательно) виртуальное окружение: `python -m venv .venv` и активация
   (`.venv\Scripts\activate` в Windows, `source .venv/bin/activate` в Linux/macOS).
4. Внешних зависимостей нет; если появятся — добавить их в `requirements.txt`, `build.py` установит их автоматически.

## Запуск тестов
```bash
python -m unittest discover -s tests          # все тесты
python -m unittest tests.test_integration -v  # один модуль
```
Интеграционный тест использует `data/products.json` (товар id=1, размер 40, остаток ≥ 2).
Если в интерактивном режиме остатки распроданы — восстановите файл: `git checkout data/products.json`.

## Добавление новой функции
1. Определить модуль по ответственности (`catalog`, `cart`, `orders`, `analytics`, `storage`).
2. Написать функцию с docstring; импорты только вида `from src.<модуль> import ...`, без циклов.
3. Добавить модульный тест в `tests/test_<модуль>.py`, при необходимости — сценарий в `test_integration.py`.
4. Описать функцию в `docs/17_API_Reference.md`, при необходимости — пункт меню в `main.py` и `18_User_Guide.md`.
5. Запустить `python build.py`.

## Ветки и Pull Request
```bash
git checkout -b feature/US-8-action-log
# ... изменения, тесты ...
git add .
git commit -m "US-8: журнал действий"
git push -u origin feature/US-8-action-log
```
Затем на GitHub: **Compare & pull request** → описание (что сделано, как проверить) → ревью → Merge в `main`.

## Сборка
```bash
python build.py
```
Шаги: проверка версии Python → зависимости → наличие `data/products.json` → тесты → демо-запуск `main.py --demo`.
При ошибке скрипт завершается с кодом 1, при успехе печатает «Сборка успешна!».

## Релиз
```bash
git tag -a v1.0 -m "Релиз версии 1.0"
git push origin v1.0
```
