-- key part 

-- indexing by name and score 
CREATE INDEX index_name_first_score ON names (name(1), score);
