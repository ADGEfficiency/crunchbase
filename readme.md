# Crunchbase database

[Pipeline](https://www.dataengineering.academy/) adventure to learn Python / SQLite / make / Flask / Docker using the [Crunchbase API](https://data.crunchbase.com/docs/using-the-api).

App is hosted on [Python Anywhere](http://adamg33.pythonanywhere.com/).

## Requirements

Python (Flask), SQLite, Docker


Put your Crunchbase host & key in a file `keys.py`:

```python
headers = {
    'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR-KEY-HERE"
    }
```

## Usage

Setup 

```bash
$ pip install -r requirements.txt
$ make api sql docker
```
