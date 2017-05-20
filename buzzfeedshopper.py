def get_recipe_from_link(buzzlink):

	import requests, bs4

	res = requests.get(buzzlink)
	res.raise_for_status()

	linkSoup = bs4.BeautifulSoup(res.text, 'html.parser')

	recipe_parent = linkSoup.find_all('span', string='INGREDIENTS')[0].parent.parent

	recipe_elems = recipe_parent.find_all("p")

	recipe_list = []

	for element in recipe_elems:
		recipe_list.append(element.text)

	#print(recipe_list)
	return recipe_list


def send_to_wunderlist(recipe_list):

	import smtplib
	import credentials

	gmail_user = credentials.login['email']
	gmail_pwd = credentials.login['password']

	FROM = gmail_user
	TO = 'me@wunderlist.com'

	for item in recipe_list:
		SUBJECT = item

		# Prepare actual message
		message = """From: %s\nTo: %s\nSubject: %s\n""" % (FROM, TO, SUBJECT)

		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.login(gmail_user, gmail_pwd)
			server.sendmail(FROM, TO, message)
			server.close()
			print('successfully sent the mail')
		except:
			print('failed to send mail')


def main():

	recipe_list = get_recipe_from_link('http://bzfd.it/2qnU88I')
	send_to_wunderlist(recipe_list)


if __name__ == "__main__":
	main()
