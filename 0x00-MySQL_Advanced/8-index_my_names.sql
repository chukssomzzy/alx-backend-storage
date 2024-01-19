-- indexing 

-- Create an index with the first character of names 
CREATE INDEX first_letter ON names (name(1));
