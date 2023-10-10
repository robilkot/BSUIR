#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <fcntl.h>

void CopyFile(char* sourceName, char* destName) {
    int source, dest;
    char buffer[4096];
    ssize_t bytes_read;
    struct stat statbuf;

    source = open(sourceName, O_RDONLY);
    if (source == -1) {
        printf("couldn't open file\n");
        return;
    }

    dest = open(destName, O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
    if (dest == -1) {
        printf("couldn't write file\n");
        return;
    }

    if (fstat(source, &statbuf) == -1) {
        printf("couldn't get permissions from file\n");
        return;
    }

    if (fchmod(dest, statbuf.st_mode) == -1) {
        printf("couldn't set permissions for file\n");
        return;
    }

    while ((bytes_read = read(source, buffer, 4096)) > 0) {
        if (write(dest, buffer, bytes_read) != bytes_read) {
            printf("couldn't write file\n");
        return;
        }
    }

    close(source);
    close(dest);
}

int main(int argc, char** argv) {

    __pid_t mainPid = getpid();

    size_t processesNumber = 0;
    size_t ProcessesNumberLimit = 2;

    char* firstFolderName[256];
    char* secondFolderName[256];

    printf("Enter 1st folder name\n");
    scanf("%s",firstFolderName);
    DIR* dir1 = opendir(firstFolderName);
    if (dir1 == 0) {
        perror("Cannot open 1ds directory");
        exit(-1);
    }

    printf("Enter 2nd folder name\n");
    scanf("%s",secondFolderName);
    DIR* dir2 = opendir(secondFolderName);
    if (dir2 == 0) {
        perror("Cannot open 2nd directory");
        exit(-1);
    }

    printf("Enter processes number limit\n");
    scanf("%d",&ProcessesNumberLimit);

    struct dirent* firstFile;
    while ((firstFile = readdir(dir1)) != 0 && getpid() == mainPid) {
        char* secondFileName[512];
        strcpy(secondFileName, secondFolderName);
        strcat(secondFileName, firstFile->d_name);

        struct stat buffer;
        if (stat(secondFileName, &buffer) == -1) {
            processesNumber++;

            pid_t pid = fork();
            if (pid == 0) {
                char* firstFileName[512];
                strcpy(firstFileName, firstFolderName);
                strcat(firstFileName, firstFile->d_name);

                CopyFile(firstFileName, secondFileName);

                struct stat copiedFileStat;
                if(stat(secondFileName, &copiedFileStat) == 0) {
                    printf("Copied \"%s\" (%d bytes) (getppid: %d, getpid: %d)\n", secondFileName, copiedFileStat.st_size, getppid(), getpid());
                }
            } else if (pid > 0) {
                if (processesNumber >= ProcessesNumberLimit) {
                    int status;
                    wait(&status);
                    --processesNumber;
                }
            } else {
                perror("fork failed");
                exit(-1);
            }
        }
    }

    if(mainPid == getpid()) {
        while(wait(NULL) > 0); // Wait for all children to finish
        closedir(dir1);
        closedir(dir2);
    }
}