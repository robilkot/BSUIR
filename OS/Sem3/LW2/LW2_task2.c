#include <stdio.h>
#include <unistd.h> 
#include <time.h>

void PrintProcessInfo(char* procName) {
    printf ("%s \tgetppid: %d,\tgetpid: %d\n", procName, getppid(), getpid());
}

int main() {
    PrintProcessInfo("Parent");
    __pid_t parentPid = getpid();

    if(fork() == 0) {
        PrintProcessInfo("Child1");
    } else {
        if(fork() == 0) {
            PrintProcessInfo("Child2");
        }
    }
    
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    printf("%d: %d-%02d-%02d %02d:%02d:%02d\n", getpid(), tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);

    if(getpid() == parentPid) {
        system("ps -x");
    }
}