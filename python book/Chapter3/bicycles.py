bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[3].title())
#by asking for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1].title())

#Using individual values from the list
message = f"My first bike was a {bicycles[3].title()}."
print(message)