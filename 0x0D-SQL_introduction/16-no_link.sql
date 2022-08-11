-- Lists all rows with name attributes
-- with scores in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
