#include <stddef.h>
#include "lists.h"

int compare_lists(listint_t *head1, listint_t *head2);
void reverse_list(listint_t **head_ref);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head;
listint_t *second_half, *prev_of_slow_ptr = *head;
listint_t *midnode = NULL;
int res = 1;
if (*head != NULL && (*head)->next != NULL)
{
while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
prev_of_slow_ptr = slow_ptr;
slow_ptr = slow_ptr->next;
}
if (fast_ptr != NULL)
{
midnode = slow_ptr;
slow_ptr = slow_ptr->next;
}
second_half = slow_ptr;
prev_of_slow_ptr->next = NULL;

reverse_list(&second_half);
res = compare_lists(*head, second_half);

reverse_list(&second_half);

if (midnode != NULL)
{
prev_of_slow_ptr->next = midnode;
midnode->next = second_half;
}
else
prev_of_slow_ptr->next = second_half;
}

return (res);
}

/**
 * reverse_list - reverses a linked list
 * @head_ref: double pointer to the head of the list
 */

void reverse_list(listint_t **head_ref)
{
listint_t *prev = NULL;
listint_t *current = *head_ref;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head_ref = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if identical, 0 otherwise
 */

int compare_lists(listint_t *head1, listint_t *head2)
{
listint_t *temp1 = head1;
listint_t *temp2 = head2;

while (temp1 && temp2)
{
if (temp1->n == temp2->n)
{
temp1 = temp1->next;
temp2 = temp2->next;
}
else
return (0);
}

if (temp1 == NULL && temp2 == NULL)
return (1);

return (0);
}
