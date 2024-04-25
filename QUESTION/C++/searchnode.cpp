#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
};

void insert(Node** head, int x) {
    Node* newNode = new Node;
    newNode->data = x;
    newNode->next = *head;
    *head = newNode;
}

bool searchLinkedList(Node* head, int x) {
    Node* current = head;
    while (current != NULL) {
        if (current->data == x) {
            return true;
        }
        current = current->next;
    }
    return false;
}

int main() {
    Node* head = NULL;
    int n;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        int a;
        cin>>a;
        insert(&head, a);
    }
    int x;
    cin>>x;
    if (searchLinkedList(head, x)) {
        cout << "true" <<endl;
    } else {
        cout << "false" << endl;
    }
   
    return 0;
}