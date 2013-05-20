SELECT term from frequency
WHERE docid='10398_txt_earn' and count=1
UNION
SELECT term from frequency
WHERE docid='925_txt_trade' and count=1;
