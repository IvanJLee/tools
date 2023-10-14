#Java Environment
export JAVA_HOME_11=$(/usr/libexec/java_home -v 11)
export JAVA_HOME_17=$(/usr/libexec/java_home -v 17)
export JAVA_HOME_LASTEST=$(/usr/libexec/java_home)
export JAVA_HOME=$JAVA_HOME_11
alias jdk11="export JAVA_HOME=$JAVA_HOME_11"
alias jdk17="export JAVA_HOME=$JAVA_HOME_17"
alias jdk@lastest="export JAVA_HOME JAVA_HOME=$JAVA_HOME_LASTEST"
