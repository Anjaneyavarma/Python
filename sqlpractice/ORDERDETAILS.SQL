CREATE TABLE Details(
	Order_ID INT PRIMARY KEY,
	Product_Name VARCHAR(50) NOT NULL,
	Date_ordered DATE NOT NULL,
	time_ordered TIME NOT NULL,
	category VARCHAR(25)
);

CREATE TABLE Payment_Details(
	payment_ID INT PRIMARY KEY,
	Order_ID INT NOT NULL,
	Price INT NOT NULL, 	
	Discount INT,	
	Quantity INT,
	CONSTRAINT fk_Order_ID
		FOREIGN KEY(Order_ID)
		REFERENCES Details (Order_ID)
);

