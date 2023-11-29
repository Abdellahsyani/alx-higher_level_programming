#include "lists.h"

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

	new_node->data = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->data)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		if (current != NULL && number > current->next->data)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current = new_node;
	}
	return (new_node);
}
