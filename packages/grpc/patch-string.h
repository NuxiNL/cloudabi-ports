--- src/core/lib/surface/init.c
+++ src/core/lib/surface/init.c
@@ -19,7 +19,7 @@
 #include <grpc/support/port_platform.h>
 
 #include <limits.h>
-#include <memory.h>
+#include <string.h>
 
 #include <grpc/fork.h>
 #include <grpc/grpc.h>
