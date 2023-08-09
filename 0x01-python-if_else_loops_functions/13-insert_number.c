#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function
 * @head: arg
 * @number: arg
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *current;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
		{
			return (NULL);
		}
		(*head)->n = number;
		return (*head);
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (number <= (*head)->n)
	{
		new->next = *head;
		return (new);
	}
	
	previous = *head;
	current = (*head)->next;
	while (current != NULL)
	{
		if (number >= previous->n && number <= current->n)
		{
			previous->next = new;
			new->next = current;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	previous->next = new;
	return (new);
}
