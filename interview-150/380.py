import random
class RandomizedSet:
    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        is_exist = val not in self.num_map
        if is_exist:
            self.num_map[val] = len(self.num_map)
            self.num_list.append(val)
        return is_exist
        
    def remove(self, val: int) -> bool:
        is_exist = val in self.num_map
        if is_exist:
            idx_map = self.num_map[val]
            last_val = self.num_list[-1]
            self.num_list[idx_map] = last_val
            self.num_list.pop()
            self.num_map[last_val] = idx_map
            del self.num_map[val]
        return is_exist
        
    def getRandom(self) -> int:
        return random.choice(self.num_list)