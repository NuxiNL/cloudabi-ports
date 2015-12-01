--- pr/include/md/_unixos.h
+++ pr/include/md/_unixos.h
@@ -50,7 +50,7 @@
 #include <sys/select.h>
 #endif
 
-#ifndef SYMBIAN
+#if !defined(CLOUDABI) && !defined(SYMBIAN)
 #define HAVE_NETINET_TCP_H
 #endif
 
