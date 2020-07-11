# Client Setup

The `go/` style link relies on two things: the go.(domain) address (I'm using
go.wesleysoohoo.me) being pointed towards the golinks server and the client
having that domain in its [search
domains](https://en.wikipedia.org/wiki/Search_domain). This document will go
over how to add a domain to your search domain in different operating systems.

### Linux

Edit `/etc/resolv.conf`. On the line that says `search` replace the domain (on
my machine it is `hsd1.ca.comcast.net`) with the domain.

```
search wesleysoohoo.me
```

In some distributions of linux, the `/etc/resolv.conf` file is managed by
NetworkManager and replaced every time the computer is rebooted. To avoid this,
add a file called `/etc/resolvconf/resolv.conf.d/head` with the contents

```
search wesleysoohoo.me
```

When the `/etc/resolv.conf` file is regenerated, it will add the contents of
`/etc/resolvconf/resolv.conf.d/head` to the top of the file.

[Ask Ubuntu
Link](https://askubuntu.com/questions/584054/how-do-i-configure-the-search-domain-correctly)

### Windows


### Mac

[Apple Support
Link](https://support.apple.com/guide/mac-help/enter-dns-and-search-domain-settings-on-mac-mh14127/mac)

### iOS


### Android

