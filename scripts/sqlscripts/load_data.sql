USE book_db;

\! echo "Loading data... (this may take a while)"
\! echo "Inserting author entries"
INSERT IGNORE INTO author
  (first_name, last_name, email)
VALUES
  ('Steve', 'Roy', 'steve_roy@gmail.com'),
  ('Bob', 'Nak', 'bok-nak@yahoo.com'),
  ('Jennifer', 'Chi', 'jenn_chi@icloud.com'),
  ('Jack', 'Zee', 'jackz123@hotmail.com');

\! echo "Inserting book entries"
INSERT IGNORE INTO book
  (title, author_id)
VALUES
  ('Ghosted', 1),
  ('Into the Light', 3),
  ('Wasted', 4),
  ('Love of my Life', 3),
  ('My Wishes', 1),
  ('Greatness', 2);

source ./scripts/sqlscripts/insert_books.sql
