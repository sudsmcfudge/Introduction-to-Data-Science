SELECT docid,SUM(count) from frequency
GROUP BY docid
HAVING SUM(count)>300;
