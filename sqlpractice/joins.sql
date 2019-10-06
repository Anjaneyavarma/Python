select dept_details.dept_no, Empl_details.empl_id, Empl_details.empl_name, Empl_details.salary
from dept_details
full outer join Empl_details
on dept_details.dept_no = Empl_details.dept_no
order by dept_no
select * from dept_details


select dept_details.dept_no, Empl_details.empl_id
from dept_details 
cross join Empl_details 

select *
from dept_details
inner join Empl_details
on dept_details.dept_no = Empl_details.dept_no
where empl_id>4
order by empl_id