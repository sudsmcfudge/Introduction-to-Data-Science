SELECT docid 
FROM frequency
WHERE term='transactions'
INTERSECT
SELECT docid
FROM frequency
WHERE term='world';

SELECT DISTINCT f1.docid FROM frequency f1,frequency f2
WHERE f1.term='transactions'
AND   f2.term='world';