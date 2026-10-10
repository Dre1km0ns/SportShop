# Git Flow в проекте «СпортТовары»

## Ветки
| Ветка | Назначение | Создаётся от | Сливается в |
|---|---|---|---|
| `main` | стабильная версия продукта, релизы (теги `v*`) | — | — |
| `develop` | интеграция новых функций | `main` | `main` (релиз) |
| `feature/<название>` | отдельная функция (US-N) | `develop` | `develop` (через PR) |
| `hotfix/<название>` | срочное исправление ошибки в `main` | `main` | `main` и `develop` |

## Схема ветвления проекта
```
main      ──●────────────────────●─────────────●──  (v1.0.1)
             \                  / \            /
hotfix        \  hotfix/cart-total ●──────────┐
               \                              \
develop         ●──●───●──────●──────●────────●──●
                    \ / \    / \    /
feature    feature/low-stock  feature/total-v1, v2   feature/search-advanced
```

## Ветки занятия №7
- `feature/low-stock` — US-1, отчёт о товарах с низким остатком в `shop.py`;
- `feature/total-v1`, `feature/total-v2` — две версии `total_sum` (учебный конфликт);
- `feature/search-advanced` — US-2, доработка `search_advanced` (имитация Pull Request);
- `hotfix/cart-total` — исправление `cart_total` в `main`.

## Правила
1. В `main` не коммитим напрямую — только слияние `develop` или `hotfix/*`.
2. Сообщения коммитов: `US-N: ...` для историй, `fix: ...` для исправлений.
3. Перед слиянием запускаем `python -m unittest discover -s tests`.
4. После слияния ветка удаляется: `git branch -d <ветка>`.
