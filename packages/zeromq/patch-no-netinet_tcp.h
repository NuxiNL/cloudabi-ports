--- src/ip.cpp
+++ src/ip.cpp
@@ -38,7 +38,6 @@
 #include <sys/socket.h>
 #include <netdb.h>
 #include <netinet/in.h>
-#include <netinet/tcp.h>
 #endif
 
 #if defined ZMQ_HAVE_OPENVMS
--- src/signaler.cpp
+++ src/signaler.cpp
@@ -72,7 +72,6 @@
 
 #if !defined ZMQ_HAVE_WINDOWS
 #include <unistd.h>
-#include <netinet/tcp.h>
 #include <sys/types.h>
 #include <sys/socket.h>
 #endif
--- src/tcp.cpp
+++ src/tcp.cpp
@@ -38,7 +38,6 @@
 #include <sys/types.h>
 #include <sys/socket.h>
 #include <netinet/in.h>
-#include <netinet/tcp.h>
 #endif
 
 #if defined ZMQ_HAVE_OPENVMS
--- src/tcp_address.cpp
+++ src/tcp_address.cpp
@@ -40,7 +40,6 @@
 #ifndef ZMQ_HAVE_WINDOWS
 #include <sys/types.h>
 #include <arpa/inet.h>
-#include <netinet/tcp.h>
 #include <net/if.h>
 #include <netdb.h>
 #include <ctype.h>
--- src/tcp_listener.cpp
+++ src/tcp_listener.cpp
@@ -47,7 +47,6 @@
 #include <unistd.h>
 #include <sys/socket.h>
 #include <arpa/inet.h>
-#include <netinet/tcp.h>
 #include <netinet/in.h>
 #include <netdb.h>
 #include <fcntl.h>
