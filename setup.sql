CREATE DATABASE bookshelf;
CREATE DATABASE bookshelf_test;
CREATE USER YOUR_USERNAME WITH ENCRYPTED PASSWORD 'YOUR_USERNAME';
GRANT ALL PRIVILEGES ON DATABASE bookshelf TO YOUR_USERNAME;
GRANT ALL PRIVILEGES ON DATABASE bookshelf_test TO YOUR_USERNAME;
ALTER USER YOUR_USERNAME CREATEDB;
ALTER USER YOUR_USERNAME WITH SUPERUSER;