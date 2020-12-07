#include "lists.h"

/**
 * check_cycle - check if a linked list has a bucle
 * @list: any position of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *start = list;

	while (1)
	{
		list = list->next;

		if (start == list)
			return (1);
		if (!list)
			return (0);
	}
}
