--- ares.h
+++ ares.h
@@ -39,7 +39,7 @@
 #if defined(_AIX) || defined(__NOVELL_LIBC__) || defined(__NetBSD__) || \
     defined(__minix) || defined(__SYMBIAN32__) || defined(__INTEGRITY) || \
     defined(ANDROID) || defined(__ANDROID__) || defined(__OpenBSD__) || \
-    defined(__QNXNTO__)
+    defined(__QNXNTO__) || defined(__CloudABI__)
 #include <sys/select.h>
 #endif
 #if (defined(NETWARE) && !defined(__NOVELL_LIBC__))
