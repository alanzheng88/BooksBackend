\! echo "Creating user 'bookuser'"
CREATE USER IF NOT EXISTS 'bookuser'@'localhost' IDENTIFIED BY 'password1';
\! echo "Granting all privileges to bookuser"
GRANT ALL PRIVILEGES ON * . * TO 'bookuser'@'localhost';
\! echo "Creating database 'book_db'"
CREATE DATABASE IF NOT EXISTS book_db;
