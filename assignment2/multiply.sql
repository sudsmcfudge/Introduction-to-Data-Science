SELECT A.row_num a,B.col_num b,SUM(A.value*B.value)
FROM A JOIN B
ON A.col_num=B.row_num
GROUP BY a,b
ORDER BY A.row_num,B.col_num;