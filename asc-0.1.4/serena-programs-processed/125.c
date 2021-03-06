/*
 * C Program to Traverse the Tree Non-Recursively
 */
#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int a;
    struct node *left;
    struct node *right;
};
 
void generate(struct node **, int);
int search(struct node *, int);
void delete(struct node **);
 
int main(int argc, char *argv[])
{
    /* Serena's seed */
	int sseed;
    if (argc == 2) {
      sseed = atol(argv[1]);
    }
    srand(sseed);

    int max_actions = 100;
    int nactions = rand() % max_actions;
    
    struct node *head = NULL;
    int choice = 0, num, flag = 0, key;
 
    for (int i = 0; i < nactions; i++)
    {
      //printf("\nEnter your choice:\n1. Insert\n2. Search\n3. Exit\nChoice: ");
        choice = rand() % 2 + 1;
        switch(choice)
        {
        case 1: 
	  //printf("Enter element to insert: ");
            num = rand() % max_actions;
            generate(&head, num);
            break;
        case 2: 
	  //printf("Enter key to search: ");
            key = rand() % max_actions;
            flag = search(head, key);
            if (flag)
            {
                printf("Key found in tree\n");
            }
            else
            {
                printf("Key not found\n");
            }
            break;
        case 3: 
            delete(&head);
            printf("Memory Cleared\nPROGRAM TERMINATED\n");
            break;
        default: printf("Not a valid input, try again\n");
        }
    };
    return 0;
}
 
void generate(struct node **head, int num)
{
    struct node *temp = *head, *prev = *head;
 
    if (*head == NULL)
    {
        *head = (struct node *)malloc(sizeof(struct node));
        (*head)->a = num;
        (*head)->left = (*head)->right = NULL;
    }
    else
    {
        while (temp != NULL)
        {
            if (num > temp->a)
            {
                prev = temp;
                temp = temp->right;
            }
            else
            {
                prev = temp;
                temp = temp->left;
            }
        }
        temp = (struct node *)malloc(sizeof(struct node));
        temp->a = num;
        if (num >= prev->a)
        {
            prev->right = temp;
        }
        else
        {
            prev->left = temp;
        }
    }
}
 
int search(struct node *head, int key)
{
    while (head != NULL)
    {
        if (key > head->a)
        {
            head = head->right;
        }
        else if (key < head->a)
        {
            head = head->left;
        }
        else
        {
            return 1;
        }
    }
	return 0;
}
 
void delete(struct node **head)
{
    if (*head != NULL)
    {
        if ((*head)->left)
        {
            delete(&(*head)->left);
        }
        if ((*head)->right)
        {
            delete(&(*head)->right);
        }
        free(*head);
    }
}
