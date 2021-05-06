#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: address pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *forward;
	listint_t *backward;
	listint_t *length;
	int *list;
	int i = 0, j = 0, k = 0;

	if (!head)
		return (0);
	if (*head == NULL)
		return (1);
	forward = *head;
	backward = *head;
	length = *head;
	while (length != NULL)
	{
		length = length->next;
		i++;
	}
	list = calloc(i, sizeof(int));
	while (backward != NULL)
	{
		list[j] = backward->n;
		backward = backward->next;
		j++;
	}
	j--;
	while (forward != NULL)
	{
		if (k == j - k)
			break;
		else if (forward->n != list[j - k])
		{
			free(list);
			return (0);
		}
		forward = forward->next;
		k++;
	}
	free(list);
	return (1);
}
