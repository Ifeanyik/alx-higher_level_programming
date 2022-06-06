#include <stdlib.h>
#include "lists.h"


int is_palindrome(listint_t **head)
{
    int i = 0;
    char s[2], d[2];
    int *arr;
    listint_t *h = *head, *store;
    long unsigned int sizeguy, size_arr;
    sizeguy = sizeof((*head)->n);
    arr = calloc(1, sizeof(h->n));
    s[0] = 'y';
    d[0] = 'y';
    arr[i] = h->n;
    h = h->next;
    for(i = 1; h->next; i++)
    {
        arr = realloc(arr, sizeof(arr) + sizeguy);
        arr[i] = h->n;
        h = h->next;
    }
    size_arr = (sizeof(arr)/sizeof(sizeguy)) - 1;
    for (i = size_arr - 1; store->next; --i)
    {
        if (arr[i] != store->n)
        {
            s[0] = 'n';
            break;
        }
        store = store->next;
    }
    
    if (s[0] == d[0])
        return (1);
    else
        return (0);
}
