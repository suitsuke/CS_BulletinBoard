-- This file is run only when wanting to initialize the database.

-- Drop the posts table if it exists
DROP TABLE IF EXISTS posts;

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
