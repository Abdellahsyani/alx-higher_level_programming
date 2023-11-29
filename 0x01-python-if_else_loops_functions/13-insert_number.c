#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - the function to insert a newnode at the list.
 * @head: the head of the list.
 * @number: the number to be inserted to list.
 *
 * Return: The address of the new_node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && number > current->next->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
