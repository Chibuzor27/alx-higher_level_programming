#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - functione
 * @head: the node
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *last = NULL;
	listint_t *top = NULL;
	int is_pal = 1;

	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	last = (*head)->next;
	prev = *head;
	while(last->next != NULL)
	{
		last->prev = prev;
		prev = last;
		last = last->next;
	}
	last->prev = prev;
	top = *head;
	while (1)
	{
		if ((top == last) ||
			(top->next == last && top->n == last->n))
		{
			break;
		}
		else if (top->n == last->n)
		{
			top = top->next;
			last = last->prev;
		}
		else if (top->n != last->n)
		{
			is_pal = 0;
			break;
		}
	}
	prev = NULL;
	last = NULL;
	top = NULL;
	return (is_pal);
}
