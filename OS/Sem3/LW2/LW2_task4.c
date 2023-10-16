#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void printStatus(char* proc, int stops) {
    printf("%s pid: %d\tppid:%d", proc, getpid(), getppid());
    if(stops == 1) printf(" stops");
    if(stops == 2) printf(" execs /bin/ps");
    printf("\n");
}

int main() {
    pid_t pid1, pid2, pid3, pid4, pid5, pid6;

    printStatus("proc 0",0);
    pid1 = fork();
    if (pid1 == 0) {
        printStatus("proc 1",0);

        pid2 = fork();
        if (pid2 == 0) {
            printStatus("proc 2",2);
            execl("/bin/ps","/bin/ps",NULL,NULL);
            //execl("/bin/ps","/bin/ps","-A",NULL);

            pid3 = fork();
            if (pid3 == 0) {
                printStatus("proc 3",0);
                printStatus("proc 3",1);
                return 0;
            }
            while(wait(0)>0); // wait for proc 3
            printStatus("proc 2",1); // this won't show because execl replaces process
            return 0;
        } else {
            pid4 = fork();
            if (pid4 == 0) {
                printStatus("proc 4",0);

                pid6 = fork();
                if (pid6 == 0) {
                    printStatus("proc 6",0);
                    printStatus("proc 6",1);
                    return 0;
                }
                while(wait(0)>0); // wait for proc 6
                printStatus("proc 4",1);
                return 0;
            }
        }
        while(wait(0)>0); // wait for proc 2
        printStatus("proc 1",1);
        return 0;
    }
    while(wait(0)>0); // wait for proc 1
    printStatus("proc 0",1);
    return 0;
}