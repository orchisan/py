## socket(socket_family, socket_type, protocol = 0)
 + socket_family: `AF_UNIX` or `AF_INET`
 + socket_type  : `SOCK_STREA`M or `SOCK_DGRAM`
 + protocol     : default value 0

## method
 + 服务器
 	+ bind
 	+ listen
 	+ accept
 + 客户端
 	+ connect
 	+ connect_ex
 + 公共
 	+ recv
 	+ send
 	+ sendall
 	+ recvfrom
 	+ sendto
 	+ getpeername
 	+ getsockname
 	+ getsockopt()
 	+ setsockopt()
 	+ close
 + Blocking-Oriented Socket methos
 	+ setblocking()
 	+ settimeout()
 	+ gettimeout()
 + 面向文件的套机子函数
 	+ fileno
 	+ makefile