#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Function to reverse a linked list
ListNode* reverseLinkedList(ListNode* node) {
    ListNode* prev = nullptr;
    ListNode* curr = node;
    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}

// Function to create a linked list from user input
ListNode* createLinkedList() {
    int n;
    
    cin >> n;
    
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
    
    
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        ListNode* newNode = new ListNode(val);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = tail->next;
        }
    }
    
    return head;
}

// Function to check if a linked list is a palindrome
bool isPalindrome(ListNode* head) {
    // Find the middle of the linked list
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    slow = reverseLinkedList(slow);

    // Compare the first half with the reversed second half
    while (slow) {
        if (head->val != slow->val) {
            return false;
        }
        head = head->next;
        slow = slow->next;
    }

    return true;
}

int main() {
    ListNode* head = createLinkedList();

    if (isPalindrome(head)) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }

    return 0;
}
