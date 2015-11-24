--- libqpdf/MD5.cc
+++ libqpdf/MD5.cc
@@ -31,7 +31,6 @@
 #include <qpdf/QUtil.hh>
 
 #include <stdio.h>
-#include <memory.h>
 #include <stdlib.h>
 #include <string.h>
 #include <errno.h>
--- libqpdf/QPDF.cc
+++ libqpdf/QPDF.cc
@@ -5,7 +5,6 @@
 #include <map>
 #include <algorithm>
 #include <string.h>
-#include <memory.h>
 
 #include <qpdf/QTC.hh>
 #include <qpdf/QUtil.hh>
