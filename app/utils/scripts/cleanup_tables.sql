USE test;

-- Generate a list of all tables in the database
SET @tables = NULL;
SELECT GROUP_CONCAT(table_name) INTO @tables
FROM information_schema.tables
WHERE table_schema = 'test';

-- Prepare the dynamic SQL statement to drop all tables
SET @drop_all_tables = CONCAT('DROP TABLE IF EXISTS ', @tables);

-- Execute the dynamic SQL statement
PREPARE stmt FROM @drop_all_tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
