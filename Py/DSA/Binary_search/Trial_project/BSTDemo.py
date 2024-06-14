from datetime import datetime, timedelta

class Node:
    def __init__(self, key):
        parts = key.split(",")
        if len(parts) != 3:
            raise
        sched_time, duration, name_of_job = parts
        raw_sched_time = datetime.strptime(sched_time, "%H:%M")  
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duration))).strftime("%H:%M")
        self.data = key
        self.scheduled_end = end_time
        self.name_of_job = name_of_job.rstrip()
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Time: {self.data}, End: {self.scheduled_end}, Job: {self.name_of_job}"


class BSTDemo:

    def __init__(self):
        self.root = None

    def insert(self, key):
        try:
            if not isinstance(key, Node):
                key = Node(key)
            if self.root is None:
                self.root = key
                self.helpful_print(key, True)
            else:
                self._insert(self.root, key)
        except ValueError as e:
            print(e)

    def _insert(self, curr, key):
        key_start = datetime.strptime(key.data.strftime("%H:%M"), "%H:%M")
        key_end = datetime.strptime(key.scheduled_end, "%H:%M")
        curr_start = datetime.strptime(curr.data.strftime("%H:%M"), "%H:%M")
        curr_end = datetime.strptime(curr.scheduled_end, "%H:%M")

        if key_start >= curr_end:
            if curr.right_child is None:
                curr.right_child = key
                self.helpful_print(key, True)
            else:
                self._insert(curr.right_child, key)
        elif key_end <= curr_start:
            if curr.left_child is None:
                curr.left_child = key
                self.helpful_print(key, True)
            else:
                self._insert(curr.left_child, key)
        else:
            self.helpful_print(key, False)

    def helpful_print(self, key, succeeded):
        if succeeded:
            print(f"Added:\t\t {key.name_of_job}")            
            print(f"Begin\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print(f"-"*60)
        else:
            print(f"Rejected:\t {key.name_of_job}")            
            print(f"Begin\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print(f"Reason:\t Time slot overlap, please verify")
            print(f"-"*60)

    def in_order(self):
        '''left, root, right'''
        print("Full job schedule of today")
        print("-"*60)
        self._in_order(self.root)
        print("-"*60)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr)
            self._in_order(curr.right_child)

    def length(self):
        return self._length(self.root)

    def _length(self, curr):
        if curr is None:
            return 0
        return 1 + self._length(curr.left_child) + self._length(curr.right_child)

    def find_val(self, key):
        '''Find if the value exists in the tree or not'''
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return curr
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return None

    def min_right_subtree(self, curr):
        if curr.left_child is None:
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
                    curr.scheduled_end = min_child.scheduled_end
                    curr.name_of_job = min_child.name_of_job
                    self._delete_val(curr.right_child, curr, False, min_child.data)
                elif curr.left_child is None and curr.right_child is None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child is None:
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
            return
