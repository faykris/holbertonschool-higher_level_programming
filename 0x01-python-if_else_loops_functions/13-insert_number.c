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
		if (number < tmp->n)
		{
			new = tmp;
			new->next = tmp->next;
			break;
		}
		if (tmp->next->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			break;
		}
		tmp = tmp->next;
	}
	return (new);
}
