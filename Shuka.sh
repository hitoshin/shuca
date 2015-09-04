#!/bin/sh
#

JUM='/Users/hitoshi/work/tools/juman-7.01/bin/juman'
KNP='/Users/hitoshi/work/tools/knp-4.14/bin/knp -tab'
SPL='/Users/hitoshi/work/dev/shuka/libexec/SentenceSplitter.py'
SUM='/Users/hitoshi/work/dev/shuka/lib/Shuka.py'

LENGTH=200
LENGTHBYSENTENCE=""
if [ $1 ]
then
	LENGTH=$1
fi
if [ $2 ]
then
	LENGTHBYSENTENCE="-s"
fi

#echo "${SPL} < /dev/stdin | ${JUM} | ${KNP} | ${SUM} -l ${LENGTH} ${LENGTHBYSENTENCE}"
${SPL} < /dev/stdin | ${JUM} | ${KNP} | ${SUM} -l ${LENGTH} ${LENGTHBYSENTENCE}
