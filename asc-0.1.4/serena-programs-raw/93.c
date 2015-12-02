/*
 * C Program for counting sort
 */
#include <stdio.h>

/*  Counting sort function  */
void counting_sort(int A[], int k, int n)
{
    int i, j;
    int B[n], C[k];
    for (i = 0; i <= k; i++)
        C[i] = 0;
    for (j = 1; j <= n; j++)
        C[A[j]] = C[A[j]] + 1;
    for (i = 1; i <= k; i++)
        C[i] = C[i] + C[i-1];
    for (j = n; j >= 1; j--)
    {
        B[C[A[j]]] = A[j];
        C[A[j]] = C[A[j]] - 1;
    }
    printf("The Sorted array is : ");
    for (i = 1; i <= n; i++)
        printf("%d ", B[i]);
}
/*  End of counting_sort()  */

/*  The main() begins  */
int main()
{
    int n, k = 0, i;
    printf("Enter the number of input : ");
    *(&n)=450;

    int A[n];
    printf("\nEnter the elements to be sorted :\n");
    for (i = 1; i <= n; i++)
    {
        *(&A[i])=710;
        if (A[i] > k) {
            k = A[i];
        }
    }
    counting_sort(A, k, n);
    printf("\n");
    return 0;
}
