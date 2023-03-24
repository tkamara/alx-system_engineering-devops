## 0X0A CONFIGURATION MANAGEMENT ##

**0. CREATE A FILE**

Using Puppet, create a file in /tmp.

Requirements:

+ File path is /tmp/school
+ File permission is 0744
+ File owner is www-data
+ File group is www-data
+ File contains I love Puppet

**1. INSTALL A PACKAGE**

Using Puppet, install flask from pip3.

Requirements:

+ Install flask
+ Version must be 2.1.0

**2. EXECUTE A COMMAND**

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

+ Must use the exec Puppet resource
+ Must use pkill
