# Crunchbase database

[Pipeline](https://www.dataengineering.academy/) adventure to learn Python / SQLite using the [Crunchbase API](https://data.crunchbase.com/docs/using-the-api).

## Requirements

Python, SQLite

```
$ pip install -r requirements.txt
```

Put your host & key in a file `keys.py`:

```python
headers = {
    'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR-KEY-HERE"
    }
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

Group-by city:

```
$ /usr/bin/sqlite3 db.sqlite < group-city.sql
```

## Deployment

After setting up `db.sqlite`:

```bash
docker build -t crunch:latest .

docker run -d -p 5000:5000 crunch
```
