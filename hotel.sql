CREATE SCHEMA IF NOT EXISTS `hotel_reservation` DEFAULT CHARACTER SET utf8;


CREATE TABLE IF NOT EXISTS `hotel_reservation`.`hotels` (
  `hotelID` INT NOT NULL,
  `hName` VARCHAR(100) NULL,
  `hAddress` VARCHAR(100) NULL,
  `hCity` VARCHAR(45) NULL,
  `hState` VARCHAR(45) NULL,
  `hZipCode` INT NULL,
  `hPhoneNumber` VARCHAR(12) NULL,
  `hRating` DECIMAL(5) NULL,
  `hBestFor` VARCHAR(100) NULL,
  PRIMARY KEY (`hotelID`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotel_reservation`.`reservation` (
  `reservationID` varchar(15) NOT NULL,
  `hotel_name` varchar(45) not null,
  `hotel_city` varchar(45) not null,
  `DateFrom` varchar(45) not null,
  `DateTo` varchar(45) not null,
  `rRoomCount` varchar(2) NULL,
  `ameneties` varchar(200) null,
  `room_type` varchar(100) NOT NULL,
  PRIMARY KEY (`reservationID`)
  )
;



CREATE TABLE IF NOT EXISTS `hotel_reservation`.`rooms` (
  `roomsID` INT NOT NULL,
  `rRoomNumber` INT NULL,
  `rFloor` INT NULL,
  `rRoomType` VARCHAR(100) NULL,
  `rDescription` VARCHAR(200) NULL,
  `rRoomStatus` VARCHAR(45) NULL,
  `hotels_hotelID` INT NOT NULL,
  PRIMARY KEY (`roomsID`),
  INDEX `fk_rooms_hotels_idx` (`hotels_hotelID` ASC),
  CONSTRAINT `fk_rooms_hotels`
    FOREIGN KEY (`hotels_hotelID`)
    REFERENCES `hotel_reservation`.`hotels` (`hotelID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1110', 'Halekulani', '416 W 8th St', 'Honolulu', 'Oahu', '33040', '6835638555\n');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1111', 'Four Seasons Resort Hualalai', '616/609 St. Paul Avenue', 'Kailua Kona', 'HI', '96743', '6767945712\n');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1112', 'The Jefferson, Washington, DC', '333 Universal Hollywood Drive', 'Washington', 'DC', '20191', '5347788902');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1113', 'Montage Kapalua Bay', 'West 5th Street and Broadway', 'Lahaina', 'HI', '96738', '338814696');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1114', 'The Lodge at Sea Island', '35 South Grand Avenue', 'Sea Island', 'GA', '98032', '2715013551');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1115', 'Acqualina Resort & Spa on the Beach', '200 S Hill St', 'Sunny Isles Beach', 'FL', '33050', '7882992517');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1116', 'The Hay-Adams', '711 S Hope St', 'Washington', 'DC', '22202', '5794845232');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1117', 'Montage Deer Valley', '431 W 7th St', 'Park City', 'UT', '84020', '4491545584');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1118', 'Salisbury Hote', '123 W 57th St', 'New York', 'New York', '10019', '8887246413');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1119', 'Hotel Pennsylvania', '401 7th Ave', 'New York', 'New York', '10001', '8886758872');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1120', 'Disneyland Hotel - On Disneyland Resort Property', '1150 W Magic Way', 'Anaheim', 'CA', '92802', '8887246413');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1121', 'The Ritz-Carlton, Marina del Rey', '4375 Admiralty Way', 'Marina Del Rey', 'CA', '90292', '8886758872');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`) VALUES ('1122', 'Wilshire Condos by Barsala', '1010 Wilshire Blvd', 'Los Angeles', 'CA', '90014', '6643793510\n');


UPDATE `hotel_reservation`.`hotels` SET `hRating`='3', `hBestFor`='Families' WHERE `hotelID`='1115';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4', `hBestFor`='Pet Owners, Families' WHERE `hotelID`='1120';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4', `hBestFor`='Business Meetings' WHERE `hotelID`='1111';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5', `hBestFor`='Couples' WHERE `hotelID`='1110';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4', `hBestFor`='Families, Couples' WHERE `hotelID`='1119';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3', `hBestFor`='Pet Owners, Kids' WHERE `hotelID`='1117';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='1', `hBestFor`='Couples, Families' WHERE `hotelID`='1114';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4', `hBestFor`='Business Meetings' WHERE `hotelID`='1118';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4', `hBestFor`='Business Meetings, Families' WHERE `hotelID`='1112';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3', `hBestFor`='Couples, Pet Owners' WHERE `hotelID`='1116';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='2', `hBestFor`='Families' WHERE `hotelID`='1113';
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1134', 'The Westin Chattanooga', '801 Pine Street', 'Chattanooga', 'TN', '37402', '4657890098', '4', 'Families, Business Meetings');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1123', 'Days Inn San Jose Milpitas', '270 S Abbott Ave', 'San Jose', 'CA', '95035', '6758872123', '2', 'Business Meetings');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1124', 'The Fairmont San Jose', '170 S Market Street', 'San Jose', 'CA', '95115', '6209087652', '5', 'Pet Owners, Couples');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1125', 'Hotel Clariana', '100 E. Santa Clara St', 'San Jose', 'CA', '95145', '5794845231', '4', 'Business Meetings, Families');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1126', 'Global Luxury Suites', '101 East San Fernando Street', 'San Jose', 'CA', '95112', '5793333222', '5', 'Business Meetings, Families');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1127', 'Palmer House a Hilton Hotel', '17 E Monroe St', 'Chicago', 'IL', '60603', '8880009865', '5', 'Pet Owners, Kids');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1128', 'Staypineapple at The Alise', '12619 4th Ave Wes', 'Chicago', 'IL', '60611', '4563457654', '3', 'Business Meetings, Families');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1129', 'Central Loop Hotel', '1900 5th Ave', 'Chicago', 'IL', '60603', '8976443688', '2', 'Pet Owners, Couples');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1130', 'Kimpton Gray Hotel', '1531 7th Ave', 'Chicago', 'IL', '60602', '4565765465', '2', 'Pet Owners, Busniess Meetings');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1132', 'Club Quarters Hotel', '1400 6th Ave', 'Seattle', 'WA', '98101', '8996763476', '4', 'Couples, Families');
INSERT INTO `hotel_reservation`.`hotels` (`hotelID`, `hName`, `hAddress`, `hCity`, `hState`, `hZipCode`, `hPhoneNumber`, `hRating`, `hBestFor`) VALUES ('1133', 'Chicago Athletic Association', '721 Pine St', 'Seattle', 'WA', '98102', '6455476545', '5', 'Couples, Families');


UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.4' WHERE `hotelID`='1111';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.9' WHERE `hotelID`='1112';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='2.9' WHERE `hotelID`='1113';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='1.8' WHERE `hotelID`='1114';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3.7' WHERE `hotelID`='1115';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3.6' WHERE `hotelID`='1116';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3.5' WHERE `hotelID`='1117';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.5' WHERE `hotelID`='1118';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.4' WHERE `hotelID`='1119';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.3' WHERE `hotelID`='1120';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3.9' WHERE `hotelID`='1121';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.0' WHERE `hotelID`='1122';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='2.7' WHERE `hotelID`='1123';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5.0' WHERE `hotelID`='1124';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.1' WHERE `hotelID`='1125';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5.0' WHERE `hotelID`='1126';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5.0' WHERE `hotelID`='1127';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='3.9' WHERE `hotelID`='1128';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='2.2' WHERE `hotelID`='1129';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='2.3' WHERE `hotelID`='1130';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.8' WHERE `hotelID`='1132';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5.0' WHERE `hotelID`='1133';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='4.0' WHERE `hotelID`='1134';
UPDATE `hotel_reservation`.`hotels` SET `hRating`='5.0' WHERE `hotelID`='1110';



INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('101', '1', '1', 'Signature Suite, 1 Bedroom', 'Free WiFi, 24-hour business center', 'Available', '1110');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('102', '67', '6', 'Signature Suite, 1 Bedroom', 'Free WiFi, Breakfast available', 'Available', '1110');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('103', '68', '6', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1110');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('104', '4', '4', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1110');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('105', '5', '1', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1110');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('106', '6', '3', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1111');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('107', '7', '5', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1111');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('108', '8', '6', 'Standard Room, 1 King Bed', 'Free WiFi, Breakfast available', 'Available', '1111');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('109', '9', '5', 'Standard Room, 1 King Bed', 'Laundry service', 'Available', '1111');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('110', '10', '1', 'Room, 2 Double Beds', '24-hour business center', 'Available', '1111');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('111', '11', '2', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1112');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('112', '12', '2', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1112');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('113', '13', '2', 'Room, 2 Double Beds', '24-hour business center', 'Available', '1113');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('114', '14', '3', 'Signature Suite, 1 Bedroom', 'Free WiFi, Breakfast available', 'Available', '1113');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('115', '15', '3', 'Signature Suite, 1 Bedroom', 'Laundry service', 'Available', '1113');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('116', '16', '3', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1113');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('117', '17', '1', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1114');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('118', '18', '1', 'Club Room, Business Lounge Access', '24-hour business center', 'Available', '1114');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('119', '19', '1', 'Standard Room, 1 King Bed', 'Free WiFi, Breakfast available', 'Available', '1114');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('120', '20', '2', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1114');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('121', '21', '4', 'Room, 2 Double Beds', '24-hour business center', 'Available', '1115');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('122', '22', '3', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1115');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('123', '23', '3', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1115');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('124', '24', '3', 'Room, 2 Double Beds', '24-hour business center', 'Available', '1115');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('125', '25', '2', 'Signature Suite, 1 Bedroom', 'Laundry service', 'Available', '1116');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('126', '26', '2', 'Standard Room, 1 King Bed', '24-hour business center', 'Available', '1116');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('127', '27', '2', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1116');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('128', '28', '2', 'Club Room, Business Lounge Access', '24-hour business center\n', 'Available', '1117');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('129', '29', '3', 'Room, 2 Double Beds', 'Free WiFi, Breakfast available', 'Available', '1117');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('130', '30', '3', 'Club Room, Business Lounge Access', '24-hour business center\n', 'Available', '1117');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('131', '1', '1', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1118');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('132', '2', '1', 'Room, 2 Double Beds', '24-hour business center\n', 'Available', '1118');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('133', '3', '1', 'Signature Suite, 1 Bedroom', '24-hour business center\n', 'Available', '1118');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('134', '4', '5', 'Signature Suite, 1 Bedroom', 'Laundry service', 'Available', '1118');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('135', '5', '5', 'Room, 2 Double Beds', 'Free WiFi, Breakfast available', 'Available', '1118');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('136', '5', '5', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1119');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('137', '7', '5', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1119');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('138', '66', '6', 'Room, 2 Double Beds', 'Restaurant and bar/lounge', 'Available', '1120');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('139', '43', '4', 'Standard Room, 1 King Bed', 'Restaurant and bar/lounge', 'Available', '1121');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('140', '34', '3', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1122');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('141', '35', '3', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1122');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('142', '36', '3', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1122');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('143', '38', '3', 'Luxury Villa, 2 Bedrooms', 'Restaurant and bar/lounge', 'Available', '1122');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('144', '56', '5', 'Club Room, Business Lounge Access', 'Laundry service', 'Available', '1123');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('145', '55', '5', 'Luxury Villa, 2 Bedrooms', 'Restaurant and bar/lounge', 'Available', '1123');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('146', '53', '5', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1123');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('147', '54', '5', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1124');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('148', '34', '3', 'Luxury Villa, 2 Bedrooms', 'Restaurant and bar/lounge', 'Available', '1125');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('149', '11', '1', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1126');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('150', '15', '1', 'Club Room, Business Lounge Access', 'Free WiFi, Breakfast available', 'Available', '1127');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('151', '16', '1', 'Signature Suite, 1 Bedroom', 'Free WiFi, Breakfast available', 'Available', '1127');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('152', '765', '7', 'Signature Suite, 1 Bedroom', 'Laundry service', 'Available', '1128');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('153', '999', '9', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1129');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('154', '98', '3', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1129');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('155', '76', '3', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1129');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('156', '67', '1', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1130');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('157', '56', '3', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1130');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('158', '57', '4', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1132');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('159', '78', '3', 'Signature Suite, 1 Bedroom', 'Restaurant and bar/lounge', 'Available', '1132');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('160', '99', '2', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1132');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('161', '780', '3', 'Signature Suite, 1 Bedroom', '24-hour business center', 'Available', '1133');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('162', '456', '6', 'Luxury Villa, 2 Bedrooms', 'Free WiFi, Breakfast available', 'Available', '1134');
INSERT INTO `hotel_reservation`.`rooms` (`roomsID`, `rRoomNumber`, `rFloor`, `rRoomType`, `rDescription`, `rRoomStatus`, `hotels_hotelID`) VALUES ('100', '56', '5', 'Luxury Villa, 2 Bedrooms', 'Free WiFi', 'Available', '1110');