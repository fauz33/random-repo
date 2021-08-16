#!/bin/bash

#List files which more than 10GB
find / -type f -size +10G -exec ls -lrth {} \; > /tmp/list_of_bigfiles.txt

curl -s --user 'api:key-a843f97bd930e975ae5ffasabdf' \
	https://api.mailgun.net/v3/sandboxa6e0d0742c4a813d4a12334234.mailgun.org/messages \
	-F from='mailgun@sandboxa6e0d0742c4a813d4a12334234.mailgun.org' \
	-F to=alarm@animapoint.net. \
	-F subject='List of big files' \
	-F text='Attached list of big files'
	-F attachment=@/tmp/list_of_bigfiles.txt


