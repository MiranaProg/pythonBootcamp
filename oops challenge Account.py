class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance= balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        #return (f'your current balance is : {self.balance}')

    def withdraw(self, with_amount):
        if self.balance < with_amount:
            return 'low balance!!!'
        else:
            self.balance -= with_amount
            return (f'your current balance is : {self.balance}')
    def __str__(self):#magic method concept
        return 'Account Owner : {}'.format(self.owner) + '\nAvailable Amount : ${}'.format(self.balance)


mini = Account('mini' , 1000)
ash = Account('ash' , 3000)
mini.deposit(1000)
print(f'mini your current balance is : {mini.balance}')
print(ash.withdraw(200))

print(ash.__str__())


'''output:
mini your current balance is : 2000
your current balance is : 2800
Account Owner : ash
Available Amount : $2800

'''