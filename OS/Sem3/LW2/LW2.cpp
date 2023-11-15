#include <stdio.h> 
#include <unistd.h>

int main()
{
    pid_t pid; /* идентификатор процесса */
    printf("Пока всего один процесс\n");
    pid = fork(); /* создание нового процесса */
    printf("Уже два процесса\n");
    if (pid == 0) {
        printf("Это Дочерний процесс, его pid=%d\n", getpid());
        printf("А pid его Родительского процесса=%d\n", getppid());
    }
    else if (pid > 0)
        printf("Это Родительский процесс pid=%d\n", getpid());
    else
        printf("Ошибка вызова fork, потомок не создан\n");
}
