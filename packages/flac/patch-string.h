--- src/libFLAC/cpu.c
+++ src/libFLAC/cpu.c
@@ -36,7 +36,7 @@
 
 #include "private/cpu.h"
 #include <stdlib.h>
-#include <memory.h>
+#include <string.h>
 #ifdef DEBUG
 # include <stdio.h>
 #endif
