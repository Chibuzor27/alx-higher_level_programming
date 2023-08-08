#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function to check if list is a cycle
 * @list: the list
 *
 * Return: 1 if cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *next;

	if (list == NULL)
	{
		return (0);
	}

	next = list;
	while (next)
	{
		if (next->parsed)
		{
			return (1);
		}
		next->parsed = 1;
		next = next->next;
	}
	return (0);
}
