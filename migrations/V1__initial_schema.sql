CREATE TABLE `account` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `login` VARCHAR(16) NOT NULL
);

CREATE TABLE `image` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `query` VARCHAR(255),
  `account_id` INT,
  FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
);