-- This file is run only when wanting to initialize the database.

-- Drop the posts table if it exists
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
/*
Create a new table named posts with the following columns:
- id: Primary key, auto-incremented
- created: Timestamp with the current timestamp as default value
- title: Text field for the post title
- content: Text field for the post content
*/
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
-- Create table for user ids
-- Add timestamp for last login for monitoring of user activity
-- admin = 1, not admin = 0, could boolean be better?
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL,
    admin INTEGER
);

