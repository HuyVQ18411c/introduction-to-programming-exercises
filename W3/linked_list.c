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
  int length;
  struct node *next;
} node;

void getAllNode(node *current) {
  while (current != NULL) {
    printf("%d\t%p\n", current->value, current->next);
    current = current->next;
  }
}

int main(void) {
  node *head;
  head = (node *)malloc(sizeof(node));
  head->value = 1;
  head->length = 1;
  head->next = (node *)malloc(sizeof(node));

  head->length += 1;

  head->next->length = head->length;
  head->next->value = 2;
  head->next->next = NULL;

  node *tail = (node *)malloc(sizeof(node));
  tail->value = 3;
  head->length += 1;

  tail->length = head->length;
  head->next->next = tail;

  getAllNode(head);

  free(head->next);
  free(tail);
  free(head);
  return 0;
}