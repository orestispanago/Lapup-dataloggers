-- CREATE USER IF NOT EXISTS'ReadOnlyUser'@'%' IDENTIFIED BY 'ReadOnlyPassword';
-- GRANT SELECT ON *.* TO 'ReadOnlyUser'@'%';
-- FLUSH PRIVILEGES;
CREATE SCHEMA IF NOT EXISTS `lapupdb`;
CREATE TABLE `lapupdb`.`rsi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Datetime_UTC` DATETIME NOT NULL,
  `RECORD` INT NULL,
  `GHI_final_min` FLOAT NULL,
  `DNI_final_min` FLOAT NULL,
  `DHI_final_min` FLOAT NULL,
  `Sensor_Temp_Avg` FLOAT NULL,
  `LoggerVoltage_Min` FLOAT NULL,
  `LoggerTemp_C_Max` FLOAT NULL,
  `Error_Max` FLOAT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `Datetime_UTC_UNIQUE` (`Datetime_UTC` ASC) VISIBLE
);
-- INSERT INTO `lapupdb`.`rsi` (
--     `Datetime_UTC`,
--     `RECORD`,
--     `GHI_final_min`,
--     `DNI_final_min`,
--     `DHI_final_min`,
--     `Sensor_Temp_Avg`,
--     `LoggerVoltage_Min`,
--     `LoggerTemp_C_Max`,
--     `Error_Max`
--   )
-- VALUES (
--     '2022-12-12 11:15:00',
--     '4327622',
--     '194.86802673339844',
--     '0.0',
--     '199.25497436523438',
--     '18.3',
--     '12.14',
--     '25.1',
--     '0'
--   );
CREATE TABLE `lapupdb`.`nilu` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Datetime_UTC` DATETIME NOT NULL,
  `UV_301nm` FLOAT NULL,
  `UV_312nm` FLOAT NULL,
  `UV_320nm` FLOAT NULL,
  `UV_340nm` FLOAT NULL,
  `UV_380nm` FLOAT NULL,
  `PAR` FLOAT NULL,
  `temp_int_C` FLOAT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `Datetime_UTC_UNIQUE` (`Datetime_UTC` ASC) VISIBLE
);
-- INSERT INTO `lapupdb`.`nilu` (
--     `Datetime_UTC`,
--     `UV_301nm`,
--     `UV_312nm`,
--     `UV_320nm`,
--     `UV_340nm`,
--     `UV_380nm`,
--     `PAR`,
--     `temp_int_C`
--   )
-- VALUES (
--     '2022-12-12 12:50:00',
--     '611.0',
--     '39090.0',
--     '35860.0',
--     '71280.0',
--     '14620.0',
--     '59270.0',
--     '50.0'
--   );
CREATE TABLE `lapupdb`.`new_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `table_name` VARCHAR(45) NULL,
  `last_record_utc` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `table_name_UNIQUE` (`table_name` ASC) VISIBLE
);
INSERT INTO `lapupdb`.`last_records` (`table_name`)
VALUES ('rsi');
INSERT INTO `lapupdb`.`last_records` (`table_name`)
VALUES ('nilu');