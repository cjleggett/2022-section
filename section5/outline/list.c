#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string book;
    struct node *next;
}
node;

#define LIST_SIZE 2

bool search(string book, node *list);
bool unload(node *list);
void visualizer(node *list);

int main(void)
{
    // TODO: Create empty list

    // Add items to list
    for (int i = 0; i < LIST_SIZE; i++)
    {
        string book = get_string("Enter a new book: ");

        // TODO: add book to new node in list
        list = add_book(book, list);
    }

    // Visualize list after adding nodes.
    visualizer(list);

    // Search for book in list
    string search_book = get_string("book to search for: ");
    if (search(search_book, list))
    {
        printf("Recognized the book.\n");
    }
    else
    {
        printf("Did not recognize the book.\n");
    }

    // Free all memory used
    if (!unload(list))
    {
        printf("Error freeing the list.\n");
        return 1;
    }

    printf("Freed the list.\n");
    return 0;
}

node* add_book(string book, node *list)
{
    // TODO: add new book to beginning of list
    return list;
}

bool search(string book, node *list)
{
    // TODO: Search linked list for book
    return false;
}

bool unload(node *list)
{
    // TODO: Free all allocated nodes
    return false;
}

void visualizer(node *list)
{
    printf("\n+-- List Visualizer --+\n\n");
    while (list != NULL)
    {
        printf("Location %p\nbook: \"%s\"\nNext: %p\n\n", list, list->book, list->next);
        list = list->next;
    }
    printf("+---------------------+\n\n");
}