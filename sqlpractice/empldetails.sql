use employeDB

create table dept_details(
	dept_no INT PRIMARY KEY ,
	dept_name VARCHAR(50) NOT NULL,
	loc VARCHAR(50) 
);

create table Empl_details(
	empl_id INT PRIMARY KEY,
	dept_no INT ,
	empl_name VARCHAR(50) NOT NULL,
	salary INT,
	CONSTRAINT fk_dept_no
		FOREIGN KEY(dept_no)
		REFERENCES dept_details (dept_no)
);