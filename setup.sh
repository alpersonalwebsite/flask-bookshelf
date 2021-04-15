# to dump the data in the database from the books.psql file
bash -c "psql < setup.sql"
bash -c "psql bookshelf_test < books.psql"