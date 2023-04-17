CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Settings`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `setting` TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `setting_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`setting_id`) REFERENCES `Settings`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
);

INSERT INTO `Metals` VALUES (null, "14K Gold", 700);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1000);
INSERT INTO `Metals` VALUES(null, "Platinum", 800);
INSERT INTO `Metals` VALUES(null, "Palladium", 1200);

INSERT INTO `Styles` VALUES(null, "Classic", 500);
INSERT INTO `Styles` VALUES(null, "Modern", 600);
INSERT INTO `Styles` VALUES(null, "Vintage", 950);

INSERT INTO `Settings` VALUES(null, "Ring", 25);
INSERT INTO `Settings` VALUES(null, "Earrings", 50);
INSERT INTO `Settings` VALUES(null, "Necklace", 50);

INSERT INTO `Sizes` VALUES(null, 0.5, 400);
INSERT INTO `Sizes` VALUES(null, 0.75, 700);
INSERT INTO `Sizes` VALUES(null, 1, 1400);
INSERT INTO `Sizes` VALUES(null, 1.5, 1950);
INSERT INTO `Sizes` VALUES(null, 2, 3000);

INSERT INTO `Orders` VALUES(null, 3, 3, 3, 2);
INSERT INTO `Orders` VALUES(null, 1, 3, 2, 2);
INSERT INTO `Orders` VALUES(null, 1, 1, 1, 1);


SELECT
    o.id,
    o.metal_id,
    o.style_id,
    o.setting_id,
    o.size_id
    FROM Orders o