\! echo "Removing user 'bookuser'"
DROP USER IF EXISTS 'bookuser'@'localhost';
\! echo "Removing database 'book_db'"
DROP DATABASE IF EXISTS book_db;
