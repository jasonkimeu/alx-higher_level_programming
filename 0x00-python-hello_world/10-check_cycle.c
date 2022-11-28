#include "lists.h"
/**
 * check_cycle - fn to check linkedlist cycle
 * @list: pointer to the first item
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

		return (0);
}
