-- QUERY bands glam rock 

-- SELECT WHERE 
SELECT
band_name,
(IFNULL(split, 2022) - formed) AS lifespan, 
FROM
metal_bands 
WHERE
style LIKE '%glam rock%' 
ORDER BY 
lifespan DESC;
