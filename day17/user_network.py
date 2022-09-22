class user:
    def follows(self, user):
        user.follower = 1

def add_follower(user):
    user.follower += 1

jenny = user()
ken = user()

ken.follows(jenny)
print(jenny.follower)

add_follower(jenny)
print(jenny.follower)