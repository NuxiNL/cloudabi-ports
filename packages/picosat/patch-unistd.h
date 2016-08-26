--- picosat.c
+++ picosat.c
@@ -8147,7 +8147,7 @@
 #ifndef NGETRUSAGE
 #include <sys/time.h>
 #include <sys/resource.h>
-#include <sys/unistd.h>
+#include <unistd.h>
 #endif
 
 double
