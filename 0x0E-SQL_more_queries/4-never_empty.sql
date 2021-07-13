-- 3. Always a name
-- script that creates the table force_name on your MySQL server

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT(11) DEFAULT 1,
	name VARCHAR(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;	
