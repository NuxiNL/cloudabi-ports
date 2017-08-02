--- src/core/lib/iomgr/socket_utils_common_posix.c
+++ src/core/lib/iomgr/socket_utils_common_posix.c
@@ -43,7 +43,9 @@
 #include <fcntl.h>
 #include <limits.h>
 #include <netinet/in.h>
+#ifndef __CloudABI__
 #include <netinet/tcp.h>
+#endif
 #include <stdio.h>
 #include <string.h>
 #include <sys/socket.h>
--- src/core/lib/iomgr/tcp_server_posix.c
+++ src/core/lib/iomgr/tcp_server_posix.c
@@ -45,7 +45,9 @@
 #include <errno.h>
 #include <fcntl.h>
 #include <netinet/in.h>
+#ifndef __CloudABI__
 #include <netinet/tcp.h>
+#endif
 #include <string.h>
 #include <sys/socket.h>
 #include <sys/stat.h>
--- src/core/lib/iomgr/udp_server.c
+++ src/core/lib/iomgr/udp_server.c
@@ -46,7 +46,9 @@
 #include <fcntl.h>
 #include <limits.h>
 #include <netinet/in.h>
+#ifndef __CloudABI__
 #include <netinet/tcp.h>
+#endif
 #include <string.h>
 #include <sys/socket.h>
 #include <sys/stat.h>
