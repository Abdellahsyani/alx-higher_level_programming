#include "lists.h"

/**
 * check_cycle - the function to check about cycling
 * @list: The list to store the value
 *
 * Return: 0 if seccess, 1 if faile
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
	{
		return (0);
	}
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
