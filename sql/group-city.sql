.timer on
CREATE INDEX row_number ON crunch(city_name);
SELECT city_name, COUNT(city_name) FROM crunch GROUP BY city_name;
