USE `mydb`;

DROP PROCEDURE IF EXISTS insert_ticket;

DELIMITER //
CREATE PROCEDURE insert_ticket(
    IN ticket_price DECIMAL,
    IN ticket_seat_number INT UNSIGNED,
    IN ticket_flight_id INT
)
BEGIN
    INSERT INTO ticket (price, seat_number, flight_id)
    VALUES (ticket_price, ticket_seat_number, ticket_flight_id);
END //
DELIMITER ;


DROP FUNCTION IF EXISTS get_ticket_price_statistic;

DELIMITER //
CREATE FUNCTION get_ticket_price_statistic(
    aggregate_type VARCHAR(3)
)
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(10, 2);

    IF aggregate_type = 'max' THEN
        SELECT MAX(price) INTO result FROM ticket;
    ELSEIF aggregate_type = 'min' THEN
        SELECT MIN(price) INTO result FROM ticket;
    ELSEIF aggregate_type = 'sum' THEN
        SELECT SUM(price) INTO result FROM ticket;
    ELSEIF aggregate_type = 'avg' THEN
        SELECT AVG(price) INTO result FROM ticket;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid aggregate type';
    END IF;

    RETURN result;
END //

DROP PROCEDURE IF EXISTS get_ticket_price_statistics;

CREATE PROCEDURE get_ticket_price_statistics(IN aggregate_type VARCHAR(3))
BEGIN
    SELECT get_ticket_price_statistic(aggregate_type) AS result;
END //
DELIMITER ;


DROP TABLE IF EXISTS `mydb`.`user_additional_info`;

CREATE TABLE IF NOT EXISTS `mydb`.`user_additional_info` (
  `user_id` INT NOT NULL,
  `additional_info` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_user_additional_info_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB;

DROP TRIGGER IF EXISTS before_insert_user_additional_info;

DELIMITER //
CREATE TRIGGER before_insert_user_additional_info
BEFORE INSERT ON `mydb`.`user_additional_info`
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM `mydb`.`user` WHERE `id` = NEW.`user_id`) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot insert into user_additional_info. User does not exist.';
  END IF;
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS before_update_user_additional_info;

DELIMITER //
CREATE TRIGGER before_update_user_additional_info
BEFORE UPDATE ON `mydb`.`user_additional_info`
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM `mydb`.`user` WHERE `id` = NEW.`user_id`) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot update user_additional_info. User does not exist.';
  END IF;
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS before_delete_user_additional_info;

DELIMITER //
CREATE TRIGGER before_delete_user_additional_info
BEFORE DELETE ON `mydb`.`user_additional_info`
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM `mydb`.`user` WHERE `id` = OLD.`user_id`) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot delete from user_additional_info. User does not exist.';
  END IF;
END;
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_pacet_of_user_additional_info;

DELIMITER //
CREATE PROCEDURE insert_pacet_of_user_additional_info()
BEGIN
    DECLARE counter INT DEFAULT 1;
    WHILE counter <= 10 DO
        INSERT INTO user_additional_info (user_id, additional_info)
        VALUES (counter, CONCAT('Noname', counter));
        SET counter = counter + 1;
    END WHILE;
END //
DELIMITER ;

CALL insert_pacet_of_user_additional_info();


DROP PROCEDURE IF EXISTS insert_airline_airport;

DELIMITER //
CREATE PROCEDURE insert_airline_airport(
    IN airline_name VARCHAR(45),
    IN airport_ICAO VARCHAR(4)
)
BEGIN
    DECLARE airline_id INT;
    DECLARE airport_id INT;

    SELECT id INTO airline_id FROM airline WHERE name = airline_name;
    SELECT id INTO airport_id FROM airport WHERE ICAO = airport_ICAO;

    INSERT INTO airline_airport (airline_id, airport_id) VALUES (airline_id, airport_id);
END;
//
DELIMITER ;

CALL insert_airline_airport('Qatar Airways', 'UKBB');

DROP PROCEDURE IF EXISTS delete_airline_airport;

DELIMITER //
CREATE PROCEDURE delete_airline_airport(
    IN airline_name VARCHAR(45),
    IN airport_ICAO VARCHAR(4)
)
BEGIN
    DECLARE airline_id INT;
    DECLARE airport_id INT;

    SELECT id INTO airline_id FROM airline WHERE name = airline_name;
    SELECT id INTO airport_id FROM airport WHERE ICAO = airport_ICAO;

    DELETE FROM airline_airport WHERE airline_id = airline_id AND airport_id = airport_id;
END;
//
DELIMITER ;


DROP PROCEDURE IF EXISTS create_dynamic_table;

DELIMITER //
CREATE PROCEDURE create_dynamic_table()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE col_name VARCHAR(255);
  DECLARE col_type VARCHAR(45);
  DECLARE num_columns INT;
  DECLARE i INT;
  DECLARE cur CURSOR FOR SELECT `name`, `surname` FROM `mydb`.`user`;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO col_name, col_type;
    IF done THEN
      LEAVE read_loop;
    END IF;

    SET num_columns = FLOOR(RAND() * 9) + 1;
    SET @timestamp_part = CURRENT_DATE();
    
    SET @sql_stmt = CONCAT('CREATE TABLE IF NOT EXISTS `mydb`.`', col_name, '_', col_type, '_', @timestamp_part, '` (');
    
    SET i = 1;
    WHILE i <= num_columns DO
      SET @sql_stmt = CONCAT(@sql_stmt, '`column_', i, '` ', IF(RAND() > 0.5, 'INT', 'VARCHAR(45)'), ', ');
      SET i = i + 1;
    END WHILE;
    
    SET @sql_stmt = CONCAT(@sql_stmt, '`formatted_date` DATETIME, ');

    SET @sql_stmt = LEFT(@sql_stmt, LENGTH(@sql_stmt) - 2);
    
    SET @sql_stmt = CONCAT(@sql_stmt, ') ENGINE = InnoDB;');
    
    PREPARE create_table_stmt FROM @sql_stmt;
    EXECUTE create_table_stmt;
    DEALLOCATE PREPARE create_table_stmt;

  END LOOP;

  CLOSE cur;
END //
DELIMITER ;

CALL create_dynamic_table();

DROP TRIGGER IF EXISTS before_insert_user;

DELIMITER //
CREATE TRIGGER before_insert_user
BEFORE INSERT
ON `user` FOR EACH ROW
BEGIN
    IF NEW.name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid name. Allowed names: Svitlana, Petro, Olha, Taras';
    END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS before_insert_ticket;

DELIMITER //
CREATE TRIGGER before_insert_ticket
BEFORE INSERT
ON `ticket` FOR EACH ROW
BEGIN
    IF NEW.seat_number > 100 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid seat number. Seat number cannot exceed 100.';
    END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS before_update_ticket;

DELIMITER //
CREATE TRIGGER before_update_ticket
BEFORE UPDATE
ON `ticket` FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data in the ticket table is not allowed.';
END //
DELIMITER ;
