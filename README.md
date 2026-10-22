# Каталог облачных сервисов

Учебный облачный проект по дисциплине **«Основы облачных технологий»**
(группа ИСР262дк). Справочник моделей облачного обслуживания
**IaaS / PaaS / SaaS** с примерами реальных сервисов и небольшим
веб-приложением, которое отдаёт каталог по HTTP.

## О проекте

Проект нужен, чтобы:

- объяснить разницу между моделями IaaS, PaaS и SaaS;
- показать примеры сервисов каждой модели;
- отработать на учебном приложении развёртывание на виртуальной машине и в Docker.

## Архитектура

| Компонент | Назначение | Связь с другими компонентами |
|-----------|------------|------------------------------|
| Клиент | Браузер или `curl`, отправляет HTTP-запросы | Обращается к веб-приложению по порту 5000 |
| Веб-приложение | `app.py` на Flask, обрабатывает `/` и `/services` | Берёт данные каталога и формирует ответ |
| Данные каталога | Список сервисов по категориям IaaS / PaaS / SaaS | Используются приложением в ответе `/services` |
| Конфигурация | Переменные `APP_TITLE`, `PORT`; шаблон `config/example.env` | Читается приложением при старте |

Схема: `Клиент → HTTP → Веб-приложение (Flask) → Данные каталога`

## Структура репозитория

| Путь | Назначение |
|------|------------|
| `app.py` | веб-приложение (точка запуска) |
| `requirements.txt` | зависимости Python |
| `app/` | каталог для развития исходного кода |
| `docs/service-models.md` | описание моделей IaaS / PaaS / SaaS |
| `docs/services-examples.md` | примеры облачных сервисов |
| `config/example.env` | шаблон конфигурации **без секретов** |
| `reports/` | отчёты по лабораторным работам |

## Технологии

- **Git** и **GitHub**: хранение кода, Issues, ветки, Pull Requests
- **Python 3** и **Flask**: веб-приложение
- **Markdown**: документация

## Запуск

Нужны Python 3 и Git.

1. Клонировать репозиторий и перейти в каталог проекта.
2. Создать и активировать виртуальное окружение.
3. Установить зависимости.
4. Запустить приложение.

```bash
git clone https://github.com/yamum16/cloud-team-isr262dk.git
cd cloud-team-isr262dk
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Проверка (во втором терминале):

```bash
curl http://127.0.0.1:5000
curl http://127.0.0.1:5000/services
```

Необязательные параметры задаются переменными окружения:
`PORT` (по умолчанию 5000) и `APP_TITLE`. Реальные пароли и ключи в
репозиторий **не добавляются**: см. `config/example.env`.

## Развертывание на виртуальной машине

Ubuntu Server в VirtualBox, сеть NAT с пробросом порта 5000.

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv
git clone https://github.com/yamum16/cloud-team-isr262dk.git
cd cloud-team-isr262dk
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export PORT=5000
python app.py
```

Проверка на ВМ: `curl http://127.0.0.1:5000`.
С хост-компьютера: `http://127.0.0.1:5000` (через проброс порта NAT).

Обновление после изменений в GitHub: `git status`, затем `git pull`.

## Автор

Жанашева И.М., группа ИСР262дк. Работа выполнена индивидуально.

## Ход работы

| Лабораторная | Что сделано |
|--------------|-------------|
| № 3 | Issues, ветки, Pull Requests, review — [отчёт](reports/lab3.md) |
| № 4 | Документация README, прототип приложения — [отчёт](reports/lab4.md) |
| № 6 | Развертывание из GitHub на виртуальной машине |

Справочные материалы: [модели обслуживания](docs/service-models.md),
[примеры сервисов](docs/services-examples.md),
[синтаксис Markdown на GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
