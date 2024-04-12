#include <iostream>

using namespace std;

// Define the Node structure
struct Node {
    int val;
    Node *next;
    Node(int x) : val(x), next(NULL) {}
};

// Function to reverse a linked list
Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* current = head;
    Node* next = nullptr;

    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

int main() {
    // Prompt the user to enter the length of the linked list
    int length;

    cin >> length;

    // Prompt the user to enter integers representing the linked list separated by spaces
    
    Node* head = nullptr;
    Node* current = nullptr;
    int value;

    // Construct the linked list from the input integers
    for (int i = 0; i < length; ++i) {
        cin >> value;
        Node* newNode = new Node(value);
        if (head == nullptr) {
            head = newNode;
            current = head;
        } else {
            current->next = newNode;
            current = current->next;
        }
    }

    // Reverse the linked list
    Node* reversedList = reverseList(head);

    // Print the reversed list
    
    while (reversedList != nullptr) {
        cout << reversedList->val << " ";
        reversedList = reversedList->next;
    }
    cout << endl;

    return 0;
}
