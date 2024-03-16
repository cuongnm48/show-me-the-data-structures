# Problem 1: LRU Cache

In the LRUCache implementation, both the get and set operations have a time complexity of O(1) on average, meaning their execution time remains constant regardless of the cache's size.

# Problem 2: File Recursion

Time Efficiency:
The function's time efficiency depends on the size of the directory structure. Traversal involves iterating through directories and files, and file identification checks the suffix of each file. The time complexity is O(n), where n is the total number of directories and files.

Space Efficiency:
The function stores file paths in a list and utilizes memory for recursion and stack space. Memory usage grows with the number of files found. Overall, space efficiency is reasonable for typical directory structures, but large structures may impact memory usage.

# Problem 3: Huffman Encoding

The time complexity of both encoding and decoding is O(n log n), where n is the number of unique characters in the input data.
The space complexity is also O(n), where n is the number of unique characters.

# Problem 4: Active Directory

Time Complexity: In the worst-case scenario, where the user is not found in any group or subgroup, the function traverses through every group and subgroup. Therefore, the time complexity is O(n), where n is the total number of groups and subgroups in the hierarchy.
Each instance of the Group class consumes memory for its attributes (name, groups, users). As the function traverses through the group hierarchy, it accesses and potentially creates multiple Group objects. The space complexity for storing these objects depends on the total number of groups and users in the hierarchy.

# Problem 5: Blockchain

Time Efficiency:
The calc_hash() method of the Block class computes the SHA-256 hash of the block's data, timestamp, and previous hash. This operation has a time complexity of O(n), where 'n' is the length of the concatenated string.
The add_block() method of the Blockchain class creates a new block, calculates its hash, and appends it to the block_list. This operation has a time complexity of O(1), as it involves constant-time operations such as appending to a list and invoking the calc_hash() method.
Printing the details of each block in the print_blocks() method of the Blockchain class requires iterating over each block in the block_list, which has a time complexity of O(n), where 'n' is the number of blocks in the blockchain.

Space Efficiency:
Each block object (Block instance) stores a fixed set of attributes: timestamp, data, previous hash, current hash, and a reference to the next block. Regardless of the size of the data or the number of blocks in the blockchain, the space required for each block remains constant.
The Blockchain class maintains a list (block_list) containing references to all blocks in the blockchain. This list grows linearly with the number of blocks, but each element in the list only holds a reference to a block, not the entire block itself.

# Problem 6: Union & Intersection

Time Efficiency:
Appending to Linked List: The append method of the LinkedList class iterates through the linked list until it finds the last node. The time complexity of appending is O(n), where n is the number of elements in the linked list.
Union Operation: The union function iterates through both linked lists to create two sets containing unique elements. Then, it iterates through the union set to create a new linked list. The time complexity of this operation is O(n + m), where n and m are the lengths of the input linked lists.
Intersection Operation: Similar to the union operation, the intersection function iterates through both linked lists to create two sets containing unique elements. Then, it iterates through the intersection set to create a new linked list. The time complexity of this operation is also O(n + m), where n and m are the lengths of the input linked lists.

Space Efficiency:
Appending to Linked List: Each time a node is appended to the linked list, a new node object is created. The space complexity for appending is O(1) for each element added.
Union Operation: Two sets are created to store the unique elements from each linked list, and then a new linked list is created to store the union of these sets. The space complexity for the union operation is O(n + m), where n and m are the lengths of the input linked lists.
Intersection Operation: Similar to the union operation, two sets are created to store the unique elements from each linked list, and then a new linked list is created to store the intersection of these sets. The space complexity for the intersection operation is also O(n + m), where n and m are the lengths of the input linked lists.
