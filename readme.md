# Crunchbase database

Pipeline adventure to learn Python / SQLite

## Requirements

Python, SQLite

```
pip install -r requirements.txt
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
