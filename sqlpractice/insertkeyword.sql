use Order_Details

alter table Details add Date_ordered smalldatetime NULL
alter table Details Alter column Date_ordered date
insert into Details (Order_ID, Product_Name, category) values (3,'Lotus Face Wash', 'Health and glow');
insert into Details (Order_ID, Product_Name, category, Date_ordered) values (4,'Toaster','Kitchen','2019-07-6');
insert into Details values (5,'SamsungM20','Phone','2019-7-12');