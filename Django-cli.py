# Task #01 in Django CLI

import myapp.user from User

list_of_users = User.objects.all()
print("list_of_users", list_of_users)

for user in list_of_users:
  user.delete()

print("all the user deleted successfully")
