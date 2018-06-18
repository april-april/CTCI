#credit: CTCI

from LinkedList import LinkedList


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll