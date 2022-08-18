class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        """Removes and returns the last item for the list, which is also the
        top item of the Stack.

        The runtime here is constant time, because all it does is index to the
        last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        This method returns the last item in the list, which is also item at the top of the Stack.

        This method runs in constant time because indexing into a list is done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None
        
    def size(self):
        """
        This method return sthe length of the list that is representing the Stack.

        This method runs in constanct time becaue finding the length of a list also in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """
        This method returns a Boolean value describing whether or not the Stack is empty.

        Testing for equality happens in constant time.
        """
        return self.items == []
    
    def match_symbols(sym_str):

        symbol_pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
            }

        openers = symbol_pairs.keys()
        my_stack = Stack()

        index = 0
        while index < len(sym_str):
            
            if sym_str[index] in openers:
                my_stack.push(sym_str[index])
                76
            else: # The symbol is a closer

                # If the Stack is already empty, the symbols are not balanced
                if my_stack.is_empty():
                    return False

                # If there are still items in the Stack, check for a mis-match.
                else:
                    top_item = my_stack.pop()
                    if sym_str[index] != symbol_pairs[top_item]:
                        return False
            
            index += 1

        if my_stack.is_empty():
            return True


    def __str__(self):
        return self.items.__str__()

    def __repr__(self):
        return self.items.__repr__()

if __name__ == '__main__':
    my_stack = Stack()

    print(Stack.match_symbols('[()]'))
    print(Stack.match_symbols('hello'))



