--- http.c
+++ http.c
@@ -45,7 +45,6 @@
 #include <sys/resource.h>
 #include <sys/socket.h>
 #include <sys/stat.h>
-#include <sys/wait.h>
 #else
 #include <winsock2.h>
 #include <ws2tcpip.h>
