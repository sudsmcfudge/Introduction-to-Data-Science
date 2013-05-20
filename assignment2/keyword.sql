SELECT f2.docid, SUM(f1.count*f2.count) 
FROM (
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) AS f1
JOIN (
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) AS f2
ON f1.term=f2.term
WHERE f1.docid='q'
GROUP BY f2.docid
ORDER BY -SUM(f1.count*f2.count);