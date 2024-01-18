-- Ranks country origins of bands 

-- SELECT COUNT GROUP ORDER 
SELECT
origins, 
COUNT(fans) as nb_fans 
FROM
metal_bands 
GROUP BY origins 
ORDER BY nb_fans DESC;
