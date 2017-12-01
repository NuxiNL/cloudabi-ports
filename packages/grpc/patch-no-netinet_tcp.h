--- src/core/lib/iomgr/socket_utils_common_posix.c
+++ src/core/lib/iomgr/socket_utils_common_posix.c
@@ -28,7 +28,9 @@
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
@@ -30,7 +30,9 @@
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
@@ -31,7 +31,9 @@
 #include <fcntl.h>
 #include <limits.h>
 #include <netinet/in.h>
+#ifndef __CloudABI__
 #include <netinet/tcp.h>
+#endif
 #include <string.h>
 #include <sys/socket.h>
 #include <sys/stat.h>
