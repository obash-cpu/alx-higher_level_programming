able File  3 lines (3 sloc)  154 Bytes
 

#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
