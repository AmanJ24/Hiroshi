class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None


class BSTDEMO:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)
        

    def in_order(self):
        '''left, root, right'''
        return self._in_order(self.root)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=' ')
            self._in_order(curr.right_child)

    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end= ' ')
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        '''left, right, root'''
        return self._post_order(self.root)

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end= ' ')

    def find_val(self, key):
        '''Find if the value exists in the tree or not'''
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in the tree"

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else:
            print(f"{key} not found in the tree.")

tree = BSTDEMO()

tree.insert('F')
tree.insert('C')
tree.insert('A')
tree.insert('G')
tree.insert('A')
tree.insert('B')
tree.insert('K')
tree.insert('H')
tree.insert('E')
tree.insert('D')
tree.insert('I')
tree.insert('M')
tree.insert('J')
tree.insert('L')

print(tree.in_order())
tree.delete_val('F')
print(tree.in_order())