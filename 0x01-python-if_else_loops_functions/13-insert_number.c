#include "lists.h"

/**
 * insert_node - Function that inserts a number into singly-linked list.
 * @h: A pointer.
 * @no: The number.
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **h, int no)
{
	listint_t *n_ode = *h, *e;
	e = malloc(sizeof(listint_t));
	if (e == NULL)
		return (NULL);
	e->n = no;

	if (n_ode == NULL || n_ode->n >= no)
	{
		e->next = n_ode;
		*h = e;
		return (e);
	}

	while (n_ode && n_ode->next && n_ode->next->n < no)
		n_ode = n_ode->next;

	e->next = n_ode->next;
	n_ode->next = e;

	return (e);
}
