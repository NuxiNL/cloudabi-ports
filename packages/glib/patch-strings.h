--- glib/glib-init.c
+++ glib/glib-init.c
@@ -28,6 +28,7 @@
 #include "gmem.h"       /* for g_mem_gc_friendly */
 
 #include <string.h>
+#include <strings.h>
 #include <stdlib.h>
 #include <stdio.h>
 #include <ctype.h>
--- glib/gstrfuncs.c
+++ glib/gstrfuncs.c
@@ -33,6 +33,7 @@
 #include <stdlib.h>
 #include <locale.h>
 #include <string.h>
+#include <strings.h>
 #include <locale.h>
 #include <errno.h>
 #include <ctype.h>              /* For tolower() */
