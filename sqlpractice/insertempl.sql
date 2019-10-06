insert into dept_details (dept_no, dept_name, loc) values (9,'Sales Manager','Hyderabad');
insert into Empl_details values (44,8,'AB',10000)
update dept_details set loc = 'Mumbai', dept_name = 'Sales Manager' where dept_no = 6;
update dept_details set loc = 'Banglore' where dept_no = 2;
update Empl_details set empl_id = 1 where dept_no = 6;
select * from dept_details
select top(2) * from Empl_details
select * from Empl_details
select empl_id from Empl_details
select distinct loc from dept_details
select * from dept_details order by dept_name ASC
select top(2) * from dept_details order by dept_no desc
select dept_name, loc from dept_details where dept_name = 'Accounting' And loc = 'Hyderabad'
select dept_no from dept_details where dept_no > 2 
select dept_name, loc from dept_details where dept_name = 'Accounting' or loc = 'Hyderabad'
select * from dept_details where dept_name not in ('IT','Marketing')
select * from dept_details where loc like 'B%'
select * from dept_details where loc like 'Hyd%'
select * from dept_details where loc like '%d'
select * from dept_details
select * from Empl_details
delete from Empl_details where salary = 20000
update Empl_details set dept_no = 3 where empl_id = 6
insert into Empl_details values(45,2,'hj',10000)
