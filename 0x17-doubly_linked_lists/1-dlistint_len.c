#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list
 * @h: head node
 *
 * Return: number of nodes, 0 its fails
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	if (h == NULL)
		return (i);
	while (h != NULL)
	{
		if (h->prev == NULL && i != 0)
			break;
		if (h->next == NULL)
		{
			h = h->prev;
		}
		else
		{
			h = h->next;
		}
		i++;
	}
	return (i);
}