#include <iostream>
using namespace std;

// Definition for a linked list node
struct Node {
    int data;
    Node *next;
    Node(int x) : data(x), next(nullptr) {}
};

Node* sortList(Node* head) {
    // Initialize three pointers to maintain the positions of 0s, 1s, and 2s
    Node *zeroPtr = new Node(0);
    Node *onePtr = new Node(0);
    Node *twoPtr = new Node(0);

    // Initialize three dummy nodes for each category
    Node *zeroDummy = zeroPtr;
    Node *oneDummy = onePtr;
    Node *twoDummy = twoPtr;

    Node *current = head;
    while (current) {
        if (current->data == 0) {
            zeroPtr->next = current;
            zeroPtr = zeroPtr->next;
        } else if (current->data == 1) {
            onePtr->next = current;
            onePtr = onePtr->next;
        } else {
            twoPtr->next = current;
            twoPtr = twoPtr->next;
        }
        current = current->next;
    }

    // Connect the three categories
    zeroPtr->next = oneDummy->next ? oneDummy->next : twoDummy->next;
    onePtr->next = twoDummy->next;

    // Update the last node's next to NULL to avoid loops
    twoPtr->next = NULL;

    // Return the head of the sorted list
    return zeroDummy->next;
}

// Function to print the linked list
void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    int size;
 
    cin >> size;

 
    Node* head = nullptr;
    Node* tail = nullptr;
    for (int i = 0; i < size; ++i) {
        int data;
        cin >> data;
        Node* newNode = new Node(data);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }
 

    // Sorting the linked list
    Node* sortedHead = sortList(head);

    
    printList(sortedHead);

    // Freeing memory
    Node* temp;
    while (sortedHead) {
        temp = sortedHead;
        sortedHead = sortedHead->next;
        delete temp;
    }

    return 0;
}
