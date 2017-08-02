--- src/core/lib/surface/init.c
+++ src/core/lib/surface/init.c
@@ -34,7 +34,7 @@
 #include <grpc/support/port_platform.h>
 
 #include <limits.h>
-#include <memory.h>
+#include <string.h>
 
 #include <grpc/grpc.h>
 #include <grpc/support/alloc.h>
