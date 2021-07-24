echo -n $1 | iconv -t UTF-16LE | openssl md5 > $2.txt
