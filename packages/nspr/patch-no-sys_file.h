--- pr/src/pthreads/ptio.c
+++ pr/src/pthreads/ptio.c
@@ -26,7 +26,6 @@
 #include <sys/socket.h>
 #include <sys/stat.h>
 #include <sys/uio.h>
-#include <sys/file.h>
 #include <sys/ioctl.h>
 #if defined(DARWIN)
 #include <sys/utsname.h> /* for uname */
