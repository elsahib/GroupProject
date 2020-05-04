#! /bin/bash
sleep 5
DBTABLES="`mysql -h${DBserv} -u${DBUser} -p${MYSQL_ROOT_PASSWORD} --batch -N -e "use prizes;show table status;" | gawk 'BEGIN {ORS=", " } $2 == "MyISAM" || $2 == "InnoDB"{print "\`" $1 "\`"}' | sed 's/, $//'`"
if [ -z "${DBTABLES// }" ]
then
exec python create.py
fi