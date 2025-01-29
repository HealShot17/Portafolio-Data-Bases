SELECT * FROM hello_mysql.users where email is null;

SELECT * FROM hello_mysql.users where not email is null;

SELECT * FROM hello_mysql.users where email is  not null;

SELECT * FROM hello_mysql.users where email is  not null and user_age = 15;
