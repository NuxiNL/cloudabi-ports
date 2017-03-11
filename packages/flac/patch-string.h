--- src/libFLAC/cpu.c
+++ src/libFLAC/cpu.c
@@ -37,7 +37,7 @@
 #include "private/cpu.h"
 #include "share/compat.h"
 #include <stdlib.h>
-#include <memory.h>
+#include <string.h>
 
 #if defined(_MSC_VER)
 #  include <intrin.h> /* for __cpuid() and _xgetbv() */
