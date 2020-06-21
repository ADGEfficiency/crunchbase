api:
	# Create `./data/crunchbase.csv`:
	python get_data_from_api.py

sql: ./data/crunchbase.csv
	rm -rf ./data/db.sqlite
	# Create schema & load data into `./data/db.sqlite`:
	/usr/bin/sqlite3 ./data/db.sqlite < ./sql/schema.sql
	# Add timestamp columns:
	/usr/bin/sqlite3 ./data/db.sqlite < ./sql/timestamps.sql
	# Group-by city:
	/usr/bin/sqlite3 ./data/db.sqlite < ./sql/group-city.sql

inspect: ./data/db.sqlite
	/usr/bin/sqlite3 ./data/db.sqlite < ./sql/inspect.sql

docker: ./data/db.sqlite
	docker build -t crunch:latest .
	docker run -d -p 5000:5000 crunch

app:
	python app.py
