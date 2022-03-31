#!/bin/bash

echo -e "suidcheck By Nongcloud"
echo -e "https://github.com/nongcloud/oscp-Learn"
echo -e "------------------------------"

echo -e "\033[32mSearching for executables file with s privileges \033[0m\n"

find / -perm -u=s -type f 2>/dev/null > ./.suid_check_result.txt

cat ./.suid_check_result.txt

echo -e "\n\033[32mThe results of the analysis are as follows:\033[0m"

echo -e "--------------------------------------------------------------------------"

echo -e "\033[32mSUID/Details File                           | Visit the link to see how to use it\033[0m"

printf "%-35s | %-10s\n" ----------------------------------- ------------------------------------

while read line
do
    #echo ${line##*/}
    case ${line##*/} in
        ash) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/ash.md
        ;;
        base64) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/base64.md
        ;;
        bash) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/bash.md
        ;;
        busybox) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/busybox.md
        ;;
        cat) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/cat.md
        ;;
        chmod) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/chmod.md
        ;;
        chown) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/chown.md
        ;;
        chroot) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/chroot.md
        ;;
        cp) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/cp-mv.md
        ;;
        csh) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/csh.md
        ;;
        curl) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/curl.md
        ;;
        cut) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/cut.md
        ;;
        dash) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/dash.md
        ;;
        date) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/date.md
        ;;
        dd) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/dd.md
        ;;
        docker) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/docker.md
        ;;
        env) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/env.md
        ;;
        file) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/file.md
        ;;
        find) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/find.md
        ;;
        grep) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/grep.md
        ;;
        ip) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/ip.md
        ;;
        mv) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/cp-mv.md
        ;;
        openssl) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/openssl.md
        ;;
        perl) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/perl.md
        ;;
        php) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/php.md
        ;;
        python) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/python.md
        ;;
        rsync) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/rsync.md
        ;;
        rvim) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/rvim.md
        ;;
        time) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/time-timeout.md
        ;;
        timeout) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/time-timeout.md
        ;;
        vim) printf "%-35s | %-10s\n" ${line} https://github.com/nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/Details/vim.md
        ;;
    esac
done < ./.suid_check_result.txt

rm -f ./.suid_check_result.txt
