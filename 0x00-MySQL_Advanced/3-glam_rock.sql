-- QUERY bands glam rock 

-- SELECT WHERE 
SELECT
band_name,
(split - formed) AS lifespan, 
FROM
metal_bands 
WHERE
AND
split
style LIKE '%glam rock%' 
AND 
split <= 2022
ORDER BY 
lifespan DESC;
