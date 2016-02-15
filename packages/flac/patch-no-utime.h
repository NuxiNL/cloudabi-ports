--- include/share/compat.h
+++ include/share/compat.h
@@ -110,7 +110,6 @@
 #endif
 #else
 #include <sys/types.h> /* some flavors of BSD (like OS X) require this to get time_t */
-#include <utime.h> /* for utime() */
 #endif
 
 #if defined _MSC_VER
