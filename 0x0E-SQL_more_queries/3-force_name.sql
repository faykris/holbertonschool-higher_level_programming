-- 3. Always a name
-- script that creates the table force_name on your MySQL server

CREATE TABLE IF NOT EXISTS force_name(
	id INT(11) DEFAULT NULL,
	name VARCHAR(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;	
