/* Country in which the destination is located at, key "flag" is the location or the name of the flag image*/
CREATE TABLE IF NOT EXISTS Country (
    country_id INTEGER PRIMARY KEY NOT NULL,
    country_name VARCHAR(100) NOT NULL,
    flag VARCHAR(100) NOT NULL
);

/* Destination in which trip takes place in */
CREATE TABLE IF NOT EXISTS Destination (
    destination_id INTEGER PRIMARY KEY NOT NULL,
    country INTEGER NOT NULL,
    destination_name VARCHAR(100) NOT NULL,
    FOREIGN KEY(country) REFERENCES Country (country_id)
);

/* Account */
CREATE TABLE IF NOT EXISTS Account (
    account_id INTEGER PRIMARY KEY NOT NULL,
    account_role VARCHAR(20) NOT NULL, 
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

/* Trip, connects destination with the account... Not sure if the time of "reservation" is of any use in here. */
CREATE TABLE IF NOT EXISTS Trip (
    trip_id INTEGER PRIMARY KEY NOT NULL,
    destination_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    FOREIGN KEY(destination_id) REFERENCES Destination(destination_id),
    FOREIGN KEY(account_id) REFERENCES Account(account_id)
);

/* Activity Type, e.g. skiing, surfing, scuba... possibility for glyph in the given activity */
CREATE TABLE IF NOT EXISTS Activity (
    activity_id INTEGER PRIMARY KEY NOT NULL,
    activity_name INTEGER NOT NULL
);

/* Connects activity type to the trip. Contains the description of the given activity along with the activity type */
CREATE TABLE IF NOT EXISTS TripActivity (
    trip_activity_id INTEGER PRIMARY KEY NOT NULL,
    description TEXT NOT NULL,
    activity_type INTEGER NOT NULL,
    FOREIGN KEY(activity_type) REFERENCES Activity(activity_id)
);