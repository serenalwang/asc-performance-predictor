/*
 * C Program for Depth First Binary Tree Search using Recursion
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
void DFS(struct node *);
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
        printf("\nEnter your choice:\n1. Insert\n2. Perform DFS Traversal\n3. Exit\nChoice: ");
        choice = rand() % 2 + 1;;
        switch(choice)
        {
        case 1: 
	  //printf("Enter element to insert: ");
            num = rand() % max_actions;
            generate(&head, num);
            break;
        case 2: 
            DFS(head);
            break;
        case 3: 
            delete(&head);
            //printf("Memory Cleared\nPROGRAM TERMINATED\n");
            break;
        default: 
            printf("Not a valid input, try again\n");
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
 
void DFS(struct node *head)
{
    if (head)
    {
        if (head->left)
        {
            DFS(head->left);
        }
        if (head->right)
        {
            DFS(head->right);
        }
        printf("%d  ", head->a);
    }
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
