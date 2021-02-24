# Awesome DNS Resolvers

---

credited too ookangzheng
https://gist.github.com/ookangzheng/c8fba46fe1dbcc8152e3231f53f91e86

---

## Resolver List

**No Filter**

1.  https://dns.sb (Anycast)
    2a09:: / 2a09::1
    185.222.222.222 (@853 DoT, plaintext)
    https://doh.dns.sb/dns-query (DoH)


2.  uncensored.any.dns.nixnet.xyz (Anycast)
    198.251.90.114:853 (DoT)
    https://uncensored.any.dns.nixnet.xyz/dns-query (DoH)
    198.251.90.114 (plaintext)


3.  https://dns.seby.io:8443/dnsquery (Australia)
    45.76.113.31 (@853, DoT)


4.  https://ibksturm.synology.me/ (Swiss)
    dot: ibksturm.synology.me:853
    doh: https//ibksturm.synology.me/dns-query


5.  hostname: dns.cmrg.net (Canada)
    Port: 853 or 443 or 53053
    199.58.81.218 2001:470:1c:76d::53


6.  https://odvr.nic.cz/dns-query (CZ)
    193.17.47.1 2001:148f:ffff::1 (853)
    odvr.nic.cz

7.  https://doh.applied-privacy.net/query (CZ)
    37.252.185.232 2a00:63c1:a:229::3 ( 443 or 853)
    dot1.applied-privacy.net

**Filtered**

1.  adblock.any.dns.nixnet.xyz (Anycast, blockads)
    198.251.90.89:853 (DoT)
    https://adblock.any.dns.nixnet.xyz/dns-query (DoH)
    198.251.90.89 (plaintext)


2.  resolver-eu.lelux.fi (Amsterdam)
    51.158.147.50:853 (DoT)
    https://resolver-eu.lelux.fi/dns-query
    51.158.147.50 (plaintext)


3.  dns.adguard.com (Anycast, blockads)
    176.103.130.130( 853, DoT, plaintext)
    https://dns.adguard.com/dns-query


4.  https://dns.switch.ch/dns-query (Swiss)(Filter malicious site)
    dns.switch.ch (DoT, 853)


5.  https://doh.cleanbrowsing.org/doh/security-filter/ (Anycast, block malicious domains)
    85.228.168.9 2a0d:2a00:1::2 (DoT, 853, plaintext)


6.  https://dns.quad9.net/dns-query (Anycast, block malicious domains)
    9.9.9.9 2620:fe::fe (DoT, 853, plaintext [53,9953])
    dns.quad9.net
    https://dns.quad9.net:5053/dns-query?name=quad9.net

## Other
9. https://doh.defaultroutes.de/
10. https://doh.ibr.cs.tu-bs.de
11. https://doh.bugdns.com
12. https://doh.qis.io/dns-query
16. https://appliedprivacy.net/services/dns/

Note: All resolver listed in no particular order