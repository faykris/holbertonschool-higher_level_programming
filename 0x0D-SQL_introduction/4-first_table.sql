-- 4. First table
-- script that creates a table called first_table in the current database in your MySQL server
CREATE TABLE IF NOT EXISTS first_table (
	id int(11) DEFAULT NULL,
	name varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
