CREATE TABLE `account` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `login` VARCHAR(16) NOT NULL,
  `password` VARCHAR(255),
  `email` VARCHAR(255) NOT NULL
);

CREATE TABLE `image` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `url` TEXT NOT NULL,
  `query` VARCHAR(255),
  `query_date` DATETIME,
  `account_id` INT,
  FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
);