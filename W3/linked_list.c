#include <stdio.h>
#include <stdlib.h>

/*
Arrow operator (usually used with pointer): access value of structure from pointer
Ex: 
typedef struct {
    char *name;
    int age;
} Student;

Student *student;
student = (Student*) malloc(sizeof(Student));

// student is now an address
to access 'age' value we can use the following syntax:
Dereference: (*student).age
Arrow opperator: student->age
*/

typedef struct node {
  int value;
  struct node *next;
} node;

void getAllNode(node *head) {
  while (head != NULL) {
    printf("%p\t%d\t%p\n", head, head->value, head->next);
    head = head->next;
  }
  printf("\n\n");
}

void pushNode(node *n, int value) {
  // Add new node to the end
  node *current = n;
  while (current->next != NULL) {
    current = current->next;
  }
  current->next = (node *)malloc(sizeof(node));
  current->next->value = value;
  current->next->next = NULL;
}

void popFirst(node **head) {
  if ((*head)->next == NULL) {
    free((*head));
  }
  node *oldHead = *head;
  *head = (*head)->next;
  free(oldHead);
}

void popLast(node *head) {
  if (head->next == NULL) {
    free(head);
  }
  node *current = head;
  while (current->next->next != NULL) {
    current = current->next;
  }
  free(current->next);
  current->next = NULL;
}

void popNode(node **head, int n) {
  // Pop node Nth
  node *current = *head;
  node *prevNode;
  node *backNode;
  if (n == 1) {
    return popFirst(head);
  }

  for (int i = 1; i < n - 1; i++) {
    if (current->next == NULL) {
      printf("There is no next node at index %d\n", i);
      return;
    }
    current = current->next;
  }
  prevNode = current;
  backNode = current->next->next;

  free(current->next);

  prevNode->next = backNode;
}

node *getNode(node *head, int n) {
  // Get Nth node
  node *current = head;
  for (int i = 1; i < n; i++) {
    current = current->next;
  }
  return current;
}

int main(void) {
  node *head = (node *)malloc(sizeof(node));
  head->value = 1;
  head->next = NULL;
  pushNode(head, 2);
  pushNode(head, 3);
  pushNode(head, 4);
  pushNode(head, 5);

  getAllNode(head);

  popNode(&head, 1);

  popLast(head);

  getAllNode(head);

  printf("3rd node address: %p\n", getNode(head, 3));

  return 0;
}