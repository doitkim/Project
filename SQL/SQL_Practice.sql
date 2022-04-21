/*select lastname, firstname, jobTitle from employees*/
/* select * from employees */
-- select contactLastname, contactFirstname from  customers group by contactLastName-- 
-- select * from orderdetails

-- use orderdetails

-- select orderNumber, orderLineNumber, quantityOrdered * priceEach
-- as subTotal
-- from orderdetails order by subTotal desc

-- select firstName, lastName, reportsTo from employees order by reportsTo desc

-- select lastName, firstName, jobTitle, officeCode from employees
-- where officeCode between 1 And 3

-- select lastName, firstName, officeCode from employees
-- where lastName like '%son%'

-- select lastName, firstName, officeCode from employees
-- where officeCode IN (1,3)

-- select lastName, firstName, reportsTo from employees
-- where reportsTo is null

-- select lastName, firstName, jobTitle from employees
-- where jobTitle <> 'Sales Rep'

-- select lastName, firstName, officeCode from employees
-- where officeCode > 5

-- select distinct lastName from employees order by lastName

-- select e.firstName, e.lastName from employees as e
-- order by e.firstName

-- select customerName, count(*) as cnt from customers c 
-- inner join orders o on c.customerNumber = o.customerNumber group by
-- c.customerName order by cnt desc

select orderNumber, sum(quantityOrdered) AS itemCount , sum(priceEach * quantityOrdered) AS total 
from orderdetails group by orderNumber having total > 1000 and total >=600 

