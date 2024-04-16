#include <iostream>

using namespace std;

struct Node {
    int data;
    Node *next;
    Node(int x) : data(x), next(nullptr) {}
};

Node* findMiddleNode(Node* head) {
    if (head == nullptr)  
        return nullptr;
    
    int length = 0;
    Node* current = head;
    Node* middle = head;

    while (current != nullptr) {
        if (length % 2 != 0)
            middle = middle->next;
        current = current->next;
        length++;
    }
    
    return middle;
}

Node* createLinkedListFromUser() {
    int n;
    cin >> n;
    
    if (n == 0)
        return nullptr;
    
    Node* head = nullptr;
    Node* current = nullptr;
    
    for (int i = 0; i < n; ++i) {
        int data;
        cin >> data;
        if (!head) {
            head = new Node(data);
            current = head;
        } else {
            current->next = new Node(data);
            current = current->next;
        }
    }
    
    return head;
}


void printLinkedList(Node* head) {
    Node* current = head;
    while (current) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {

    Node* head = createLinkedListFromUser();


    if (!head) {
        cout << "Linked list is empty!" << endl;
        return 0;
    }


    Node* middleNode = findMiddleNode(head);
    cout << "Middle node data: " << middleNode->data << endl;

    return 0;
}
