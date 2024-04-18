#include <iostream>
#include <unordered_set>
using namespace std;

// Definition for a linked list node
struct Node {
    int data;
    Node *next;
    Node(int x) : data(x), next(nullptr) {}
};

void removeDuplicates(Node *head) {
    if (!head) return;

    unordered_set<int> seen;
    Node *current = head;
    Node *prev = nullptr;

    while (current) {
        if (seen.find(current->data) != seen.end()) {
            // Duplicate node found, remove it
            prev->next = current->next;
            delete current;
            current = prev->next;
        } else {
            seen.insert(current->data);
            prev = current;
            current = current->next;
        }
    }
}

// Function to print the unique elements of the linked list
void printUnique(Node *head) {
    if (!head) {
        cout << " ";
        return;
    }

    Node *current = head;
    while (current) {
        cout << current->data << " ";
        current = current->next;
    }
}

int main() {
    int size;
    cin >> size;

    Node *head = nullptr;
    Node *tail = nullptr;
    for (int i = 0; i < size; ++i) {
        int data;
        cin >> data;
        Node *newNode = new Node(data);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    // Remove duplicates
    removeDuplicates(head);

    
    printUnique(head);
    cout << endl;

    // Freeing memory
    Node *temp;
    while (head) {
        temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}
