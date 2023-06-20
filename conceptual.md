### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL? 
An object relational database management system

- What is the difference between SQL and PostgreSQL? 
postgresql is an open source while sql is owned by microsoft

- In `psql`, how do you connect to a database?
\c DB_NAME

- What is the difference between `HAVING` and `WHERE`?
WHERE helps with which rows to use, HAVING determines which grouped results to keep

- What is the difference between an `INNER` and `OUTER` join?
-INNER is only for the rows that match the condition in both tables
-OUTER includes 
 Left - All of the rows from the first table (left), combined with matching rows from the second table (right).
Right - The matching rows from the first table (left), combined with all the rows from the second table (right).
Full - All the rows from both tables (left and right).

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
Left - All of the rows from the first table (left), combined with matching rows from the second table (right).

Right - The matching rows from the first table (left), combined with all the rows from the second table (right).

- What is an ORM? What do they do?
Object Relational Mapper: a piece of software designed to translate between the data representations used by databases and those used in object-oriented programming.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  the latter uses sql

- What is CSRF? What is the purpose of the CSRF token?
 A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources.

- What is the purpose of `form.hidden_tag()`?
It generates a hidden field that includes a token that is used to protect the form against CSRF attacks
