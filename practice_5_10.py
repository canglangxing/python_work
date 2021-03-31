current_users = ['Grubby','SKY','Infi','Moon','west']
new_users = ['zhou','sky','miracle','flow','Moon']
current_users_lower = ['grubby','sky','infi','moon','west']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Please enter another user name.")
    else:
        print("This user name is not in use.")