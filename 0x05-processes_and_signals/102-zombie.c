#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * CreateZombies - generates 5 zombie processes.
 * Returns: 0 on success.
 */
int CreateZombies(void)
{
    int i;
    pid_t zombiePid;

    for (i = 0; i < 5; i++)
    {
        zombiePid = fork();
        if (!zombiePid)
            return 0;

        printf("Zombie process created with PID: %d\n", zombiePid);
    }

    return 0;
}

/**
 * HangForever - creates an infinite loop to make the program hang.
 * Returns: 0.
 */
int HangForever(void)
{
    while (1)
    {
        sleep(1);
    }
    return 0;
}

/**
 * Main - entry point; creates 5 zombie processes.
 * Returns: 0 on success.
 */
int main(void)
{
    CreateZombies();
    HangForever();

    return 0;
}
