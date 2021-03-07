browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

# back button is pressed:
last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect", browsing_session[-1])
