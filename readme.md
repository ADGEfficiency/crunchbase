# Crunchbase database

[Pipeline](https://www.dataengineering.academy/) adventure to learn Python / SQLite / make / Flask / Docker using the [Crunchbase API](https://data.crunchbase.com/docs/using-the-api).

## Requirements

Python (Flask), SQLite, Docker

```bash
$ pip install -r requirements.txt
```

Put your Crunchbase host & key in a file `keys.py`:

```python
headers = {
    'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR-KEY-HERE"
    }
```

## Usage

```bash
$ make api sql docker
```

```bash
$ make app
```
