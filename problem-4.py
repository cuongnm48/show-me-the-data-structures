class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is not None and isinstance(group, Group):
        if user in group.get_users():
            return True
        for subgroup in group.get_groups():
            if is_user_in_group(user, subgroup):
                return True
    return False


# Test case
print(is_user_in_group("sub_child_user", parent))  # Output: True
print(is_user_in_group("sub_child_user", sub_child))  # Output: True
print(is_user_in_group("none_existent_user", parent))  # Output: False

# Edge case:  None or an empty string is passed as the user.
print(is_user_in_group(None, parent))  # Output: False
print(is_user_in_group("", parent))  # Output: False

# Edge case:  None or an empty string is passed as the group.
print(is_user_in_group("sub_child_user", None))  # Output: False
print(is_user_in_group("sub_child_user", ""))  # Output: False