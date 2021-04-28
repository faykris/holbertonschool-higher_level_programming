#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number of node
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	tmp = *head;
	while (tmp->next != NULL)
	{
		if (tmp->next->n == number)
			return (NULL);
		if (tmp->n == 0 && number == 0)
			return (NULL);
		else if (tmp->next->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			break;
		}
		tmp = tmp->next;
	}
	return (new);
}
