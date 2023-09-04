#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{
listint_t *s = list;
listint_t *f = list;
if (!list)
return (0);
while (s && f && f->next)
{
s = s->next;
f = f->next->next;
if (s == f)
return (1);
}
return (0);
}
