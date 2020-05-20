# Crunchbase database

[Pipeline](https://www.dataengineering.academy/) adventure to learn Python / SQLite using the [Crunchbase API](https://data.crunchbase.com/docs/using-the-api).

## Requirements

Python, SQLite

```
$ pip install -r requirements.txt
```

## Usage

Create `crunchbase.csv`:

```bash
$ python get_data_from_api.py
```

Create schema & load data into `db.sqlite`:

```bash
$ /usr/bin/sqlite3 db.sqlite < schema.sql
```

Inspect database:

```bash
$ /usr/bin/sqlite3 db.sqlite < inspect.sql
```

Add timestamp columns:
```
$ /usr/bin/sqlite3 db.sqlite < timestamps.sql
```
