class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self

        def get_middle(head):
            if not head:
                return head

            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def sorted_merge(left, right):
            if not left:
                return right
            if not right:
                return left

            if left.data <= right.data:
                result = left
                result.next = sorted_merge(left.next, right)
            else:
                result = right
                result.next = sorted_merge(left, right.next)

            return result

        def merge_sort_helper(head):
            if not head or not head.next:
                return head

            mid = get_middle(head)
            next_to_mid = mid.next
            mid.next = None

            left = merge_sort_helper(head)
            right = merge_sort_helper(next_to_mid)

            sorted_list = sorted_merge(left, right)
            return sorted_list

        self.head = merge_sort_helper(self.head)
        return self

    def merge_sorted_lists(self, other_list):
        dummy_node = Node(0)
        tail = dummy_node

        l1 = self.head
        l2 = other_list.head

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        merged_list = LinkedList()
        merged_list.head = dummy_node.next
        return merged_list


list = LinkedList()
list.append(1)
list.append(5)
list.append(8)
list.append(2)
list.append(7)
list.append(6)

print("Original list:")
list.print_list()

print("Reversed list:")
list.reverse()
list.print_list()

print("Sorted list:")
list.merge_sort()
list.print_list()

print("Second list:")
new_list = LinkedList()
new_list.append(0)
new_list.append(5)
new_list.append(7)
new_list.print_list()

print("Merged list:")
merged_list = list.merge_sorted_lists(new_list)
merged_list.print_list()
