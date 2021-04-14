# Flask BookShelf App 

Flask, SQLAlchemy and PostgreSQL.

#### Pre-requisites
Be sure you have `Python3`, `PostgreSQL` and `Node/NPM` installed on your machine.

## Install dependencies

```
pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio -y

pip3 install -r requirements.txt
```

## Create and Populate the database

1. Replace all occurrences of `YOUR_USERNAME` in `books.psql` with your active username. **Hint**: `whoami`
1. Connect to PostgreSQL: `psql postgres`
1. Run the setup: `\i setup.sql`
1. Populate data: `psql -f books.psql -U student -d bookshelf`

## Set the proper env variables and run the project

```bash
export FLASK_APP=THE_NAME_OF_YOUR_APP
export FLASK_ENV=development
flask run
```

**Note:** Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.

By default, the application runs on: `http://127.0.0.1:5000/`

<!-- ---


### Step 0: Start/Stop the PostgreSQL server
```bash
which postgres
postgres --version
# Start/stop
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop 
```
If it shows that the *port already occupied* error, run:
```bash
sudo su - 
ps -ef | grep postmaster | awk '{print $2}'
kill <PID> 
```

## Additional information
#### Running Tests
If the current exercise needs testing, navigate to the backend folder and run the following commands: 
```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```
The first time you run the tests, omit the `dropdb` command. All tests are kept in that file and should be maintained as updates are made to app functionality. 


Test:

Get books
curl http://127.0.0.1:5000/books

```
{
  "books": [
    {
      "author": "Stephen King", 
      "id": 1, 
      "rating": 5, 
      "title": "The Outsider: A Novel"
    }, 
    {
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Tara Westover", 
      "id": 4, 
      "rating": 5, 
      "title": "Educated: A Memoir"
    }, 
    {
      "author": "Jojo Moyes", 
      "id": 5, 
      "rating": 5, 
      "title": "Still Me: A Novel"
    }, 
    {
      "author": "Leila Slimani", 
      "id": 6, 
      "rating": 1, 
      "title": "Lullaby"
    }, 
    {
      "author": "Amitava Kumar", 
      "id": 7, 
      "rating": 5, 
      "title": "Immigrant, Montana"
    }, 
    {
      "author": "Madeline Miller", 
      "id": 8, 
      "rating": 2, 
      "title": "CIRCE"
    }, 
    {
      "author": "Gina Apostol", 
      "id": 9, 
      "rating": 5, 
      "title": "Insurrecto: A Novel"
    }
  ], 
  "success": true, 
  "total_books": 16
}
```

curl http://127.0.0.1:5000/books?page=2

```
{
  "books": [
    {
      "author": "Tayari Jones", 
      "id": 10, 
      "rating": 5, 
      "title": "An American Marriage"
    }, 
    {
      "author": "Jordan B. Peterson", 
      "id": 11, 
      "rating": 5, 
      "title": "12 Rules for Life: An Antidote to Chaos"
    }, 
    {
      "author": "Kiese Laymon", 
      "id": 12, 
      "rating": 1, 
      "title": "Heavy: An American Memoir"
    }, 
    {
      "author": "Emily Giffin", 
      "id": 13, 
      "rating": 4, 
      "title": "All We Ever Wanted"
    }, 
    {
      "author": "Jose Andres", 
      "id": 14, 
      "rating": 4, 
      "title": "We Fed an Island"
    }, 
    {
      "author": "Rachel Kushner", 
      "id": 15, 
      "rating": 1, 
      "title": "The Mars Room"
    }, 
    {
      "author": "Gregory Blake Smith", 
      "id": 16, 
      "rating": 2, 
      "title": "The Maze at Windermere"
    }, 
    {
      "author": "Maminga", 
      "id": 23, 
      "rating": 5, 
      "title": "Sr. FullStack Developer"
    }
  ], 
  "success": true, 
  "total_books": 16
}
```

curl http://127.0.0.1:5000/books?page=4

Based on a collection of 16 elements (books) and a page size of 8 

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

Update book

curl http://127.0.0.1:5000/books/8 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'

```
{
  "id": 8, 
  "success": true
}
```

Non existing book

curl http://127.0.0.1:5000/books/888 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

Delete book

curl -X DELETE http://127.0.0.1:5000/books/8 

```
{
  "books": [
    {
      "author": "Stephen King", 
      "id": 1, 
      "rating": 5, 
      "title": "The Outsider: A Novel"
    }, 
    {
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Tara Westover", 
      "id": 4, 
      "rating": 5, 
      "title": "Educated: A Memoir"
    }, 
    {
      "author": "Jojo Moyes", 
      "id": 5, 
      "rating": 5, 
      "title": "Still Me: A Novel"
    }, 
    {
      "author": "Leila Slimani", 
      "id": 6, 
      "rating": 1, 
      "title": "Lullaby"
    }, 
    {
      "author": "Amitava Kumar", 
      "id": 7, 
      "rating": 5, 
      "title": "Immigrant, Montana"
    }, 
    {
      "author": "Gina Apostol", 
      "id": 9, 
      "rating": 5, 
      "title": "Insurrecto: A Novel"
    }, 
    {
      "author": "Tayari Jones", 
      "id": 10, 
      "rating": 5, 
      "title": "An American Marriage"
    }
  ], 
  "deleted": 8, 
  "success": true, 
  "total_books": 15
}
```

Non exiting book

curl -X DELETE http://127.0.0.1:5000/books/888

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>422 Unprocessable Entity</title>
<h1>Unprocessable Entity</h1>
<p>The request was well-formed but was unable to be followed due to semantic errors.</p>
```

Create a new book

curl -X POST -H "Content-Type: application/json" -d '{"title":"This is a title", "author":"This is the Author", "rating":"3"}' http://127.0.0.1:5000/books   

```
{
  "books": [
    {
      "author": "Stephen King", 
      "id": 1, 
      "rating": 5, 
      "title": "The Outsider: A Novel"
    }, 
    {
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Tara Westover", 
      "id": 4, 
      "rating": 5, 
      "title": "Educated: A Memoir"
    }, 
    {
      "author": "Jojo Moyes", 
      "id": 5, 
      "rating": 5, 
      "title": "Still Me: A Novel"
    }, 
    {
      "author": "Leila Slimani", 
      "id": 6, 
      "rating": 1, 
      "title": "Lullaby"
    }, 
    {
      "author": "Amitava Kumar", 
      "id": 7, 
      "rating": 5, 
      "title": "Immigrant, Montana"
    }, 
    {
      "author": "Gina Apostol", 
      "id": 9, 
      "rating": 5, 
      "title": "Insurrecto: A Novel"
    }, 
    {
      "author": "Tayari Jones", 
      "id": 10, 
      "rating": 5, 
      "title": "An American Marriage"
    }
  ], 
  "created": 24, 
  "success": true, 
  "total_books": 16
}
``` -->