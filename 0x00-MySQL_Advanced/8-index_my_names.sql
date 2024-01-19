-- indexing 

-- Create an index with the first character of names 
CREATE INDEX idx_name_first ON names (name(1));
