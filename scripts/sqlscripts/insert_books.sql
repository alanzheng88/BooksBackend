USE book_db;

/*
  Author: Alan Zheng
  Description: Procedure which leverages existing books and authors to
				create new books in the database
  Precondition: book and author table has at least one entry
  This procedure can be ran multiple times, each time
  generating <NUMBER_OF_ENTRIES> entries with unique book titles
*/
DELIMITER $$

DROP PROCEDURE IF EXISTS insert_book_data$$

CREATE PROCEDURE insert_book_data()
BEGIN
  -- these values can change and manually assigned by user
  DECLARE NUMBER_OF_OLD_BOOK_ENTRIES INT DEFAULT 6;
  DECLARE NUMBER_OF_ENTRIES INT DEFAULT 1000;
  -- values which can change ends here

  DECLARE NUMBER_OF_AUTHOR_ENTRIES INT;

  DECLARE i INT;
  -- start count at number of books in the database
  -- so that each new entry will be unique
  SET i = (SELECT COUNT(*) + 1 FROM book);
  -- set new maximum given current number of books in database
  -- because we want NUMBER_ENTRIES entries created
  SET NUMBER_OF_ENTRIES = NUMBER_OF_ENTRIES + i;
  SET NUMBER_OF_AUTHOR_ENTRIES = (SELECT COUNT(*) FROM author);

  -- insert book entries
  WHILE i < NUMBER_OF_ENTRIES DO
	-- use existing book titles to create new book title
	SET @bookTitle = (SELECT CONCAT(title, i) 
						FROM (SELECT * FROM book 
								LIMIT NUMBER_OF_OLD_BOOK_ENTRIES) bTable 
						ORDER BY RAND() LIMIT 1);
    -- 1 <= authorId <= 4 (number of authors)
    SELECT @authorId := FLOOR(1 + (RAND() * NUMBER_OF_AUTHOR_ENTRIES)) AS id;

    INSERT IGNORE INTO book
      (title, author_id)
    VALUES
      (@bookTitle, @authorId);

	SET i = i + 1;
    
  END WHILE;

END$$

DELIMITER ;
CALL insert_book_data();
