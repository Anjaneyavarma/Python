 CREATE TABLE Savings_Accounts
(
	Customer_no INT NOT NULL,
	First_Name VARCHAR(50) NOT NULL,
	Last_Name VARCHAR(50) NOT NULL,
	
);
ALTER TABLE Savings_Accounts ADD Account_Number INT NOT NULL PRIMARY KEY
ALTER TABLE Savings_Accounts ADD Phone_No INT NOT NULL
ALTER TABLE Savings_Accounts ADD Age INT NOT NULL
ALTER TABLE Savings_Accounts ADD Branch_Code INT NOT NULL
ALTER TABLE Savings_Accounts ADD Customer_Email VARCHAR(50) 
ALTER TABLE Savings_Accounts ADD Current_Bal NUMERIC(20,2) NOT NULL
ALTER TABLE Savings_Accounts ALTER COLUMN Age INT

