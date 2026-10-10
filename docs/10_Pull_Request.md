## PR: feature/search-advanced → develop

**Что сделано:**
- `search_advanced(products, query, category=None, min_price=None, max_price=None)` — комбинированный поиск
  по подстроке названия/бренда, категории (без учёта регистра) и диапазону цены;
- добавлена проверка диапазона: при `min_price > max_price` выбрасывается `ValueError`;
- добавлен тест `test_search_advanced_bad_range`.

**Как проверить:**
```bash
git checkout feature/search-advanced
python -m unittest tests.test_catalog -v
python -c "import shop; p = shop.load_products('data/products.json'); print([x['name'] for x in shop.search_advanced(p, 'nike', max_price=5000)])"
```

**Связанные задачи:** US-2

**Ревьюер:** [ФИО ревьюера]

**Результат ревью:** замечаний нет, ветка слита в `develop`.
