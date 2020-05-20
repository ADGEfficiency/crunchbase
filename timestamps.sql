
BEGIN TRANSACTION;
	ALTER TABLE crunch ADD created_at_dt TIMESTAMP;
	UPDATE crunch SET created_at_dt = DATETIME(created_at, 'unixepoch');
END TRANSACTION;

ALTER TABLE crunch ADD updated_at_dt TIMESTAMP;
UPDATE crunch SET updated_at_dt = DATETIME(updated_at, 'unixepoch');
