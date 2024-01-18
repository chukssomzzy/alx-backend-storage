-- Ranks country origins of bands 

-- SELECT COUNT GROUP ORDER 
SELECT
origin, 
COUNT(fans) as nb_fans 
FROM
metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;
