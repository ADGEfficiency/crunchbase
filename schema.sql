CREATE TABLE IF NOT EXISTS crunch(
	permalink TEXT,
	api_path TEXT,
	web_path TEXT,
	api_url TEXT,
	name TEXT,
	stock_exchange TEXT,
	stock_symbol TEXT,
	primary_role TEXT,
	short_description TEXT,
	profile_image_url TEXT,
	domain TEXT,
	homepage_url TEXT,
	facebook_url TEXT,
	twitter_url TEXT,
	linkedin_url TEXT,
	city_name TEXT,
	region_name TEXT,
	country_code TEXT,
	created_at BIGINT,
	updated_at BIGINT
);
.mode csv
.import crunchbase.csv crunch
