#!/bin/bash
> result_sh.txt

total_requests() {
echo Total requests - $(cat "${1}" | wc -l) >> result_sh.txt
}

requests_count_by_type() {
echo Requests - count >> result_sh.txt
for type in $(cat "${1}"| awk '{print$6}' | sed 's/"//' | sort -u)
do
echo $type - $(cat "${1}" | grep $type | wc -l) >> result_sh.txt  
done
}

top_requests_by_size() {
echo Top requests by size >> result_sh.txt
cat "${1}" | sort -nr -k10 | head -10 | awk '{print $7,$9,$10}' >> result_sh.txt
}

frequent_requests_with_client_error() {
echo Most frequent requests with client error >> result_sh.txt
cat "${1}" | awk '{ if ($9>=400 && $9<500) print $1,$9,$7}' | sort -k3 | uniq -c -f 2 | sort -nrk1 | head -10 | awk '{print $2,$3,$4}' >> result_sh.txt
}

top_requests_by_size_with_server_error() {
echo Top requests by size with server error >> result_sh.txt
cat "${1}" | awk '{ if ($9>=500 && $9<600) print $1,$9,$7,$10}' | sort -nrk4 | head -10 | awk '{print $1,$3,$2}' >> result_sh.txt
}

case "$2" in
	--total-count)
		total_requests "$1"
		;;
	--by-type)
		requests_count_by_type "$1"
		;;
	--by-size)
		top_requests_by_size "$1"
		;;
	--client-err)
		frequent_requests_with_client_error "$1"
		;;
	--server-err)
		top_requests_by_size_with_server_error "$1"
		;;
	--all)
		total_requests "$1"
		echo >> result_sh.txt
		requests_count_by_type "$1"
		echo >> result_sh.txt
		top_requests_by_size "$1"
		echo >> result_sh.txt
		frequent_requests_with_client_error "$1"
		echo >> result_sh.txt
		top_requests_by_size_with_server_error "$1"
		;;		
	*)
		echo wrong option "$2" 
		;;
esac		