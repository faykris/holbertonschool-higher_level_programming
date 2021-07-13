-- 5. Unique ID
-- script that creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS unique_id(
	id INT(11) DEFAULT 1,
	name VARCHAR(256) DEFAULT NULL,
	UNIQUE (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;	
