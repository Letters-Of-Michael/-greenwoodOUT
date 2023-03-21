import streamlit as st
import pandas as pd
from IPython.display import IFrame
from PIL import Image
import matplotlib.pyplot as plt

header = st.container()
background = st.container()
dataset = st.container()
question = st.container()
Data_Development = st.container()
visualization = st.container()
inference = st.container()
copywright = st.container()

with header:
	st.title('Python_twitter Project- #greenwoodOUT')
	st.write('This is a python project that came up as a personal project to showcase my ability as a data scientist to collect, modify and wrangle data from different sources and make them into meaningful tables to draw out insights. I was able to scrape off twitter for these data about a particular hashtag that caught my attention. Using python, i was able to make, modify and create tables according to their needs for our dashboard creation.')

	with background:
		st.header("BUILD UP TO THE ANALYSIS")
		st.write("This is a personal project I embarked on to get the tweet insights about a particular #tag on twitter, It was gathered that a certian Man united player was alleged to have raped his girlfriend which cost him his job and public opinion, during this trying period, the #greenwoodOUT was used by twitter users to air theri opinions. After a year, all charges against him were dropped and to get back to the team became a problem and the same #greenwoodOUT started trending as to the #greenwoodIN one would have expected. Using python tweet scrapper on Jupyter notebook I tracked the level of engagments the tweets with this #tag received. The insights gathered are so important as the parties (Team and player) in question can use to guide their decision making and get the wider public opinion on the issue on ground.")

	with dataset:
		st.header("Data gathered using python.")
		st.write("I used the pyhton module; 'tweet scrapper' to effectively scrape out tweets with the #tag, my lines of code also included the content, RTs, likes, replies and username of the user, with this we can easily determine the tweet with the highest engagments. With the lines of code intact, I was able scrape about 2879 tweets and convert into a dataframe to allow us use pandas for certain data manipulation. From the larger dataset, I was able to draw out tables with data with highest engaging metrics from likes to RTs to replies and these tables can be viewed below.")

		st.header("Universal Table")
		st.text('Here is a table showing the total tweets with the #greenwoodOUT.')
		green_data = pd.read_csv('./image/greenwood.csv')
		st.write(green_data.head())

		st.header("Follower's Table")
		st.text('This table shows the first 5 tweets with the highest followers.')
		followers_data = pd.read_csv('./image/highest-followers.csv')
		st.write(followers_data.head())

		st.header("Likes Table")
		st.text('This table shows the first 5 tweets with the highest likes.')
		likes_data = pd.read_csv('./image/highest-likes.csv')
		st.write(likes_data.head())

		st.header("Replies Table")
		st.text('This table shows the first 5 tweets with the highest replies.')
		replies_data = pd.read_csv('./image/highest-replies.csv')
		st.write(replies_data.head())

		st.header("RTs Table")
		st.text('This table shows the first 5 tweets with the highest retweets.')
		RT_data = pd.read_csv('./image/highest-RT.csv')
		st.write(RT_data.head())

	with question:
		st.header('Analysis Background')
		st.write('In this section, I provided more insights on some important questions that could arise during and after the pandemic. This insights will be a guide to our analysis and visualization as a whole.')


		st.markdown("* **First:** How massively people engaged the #tag and to further analyze people's level of interest on each tweet made about this #tag and ways it could influence the team's decision.")
		st.markdown('* **Second:** Draw out tweets with highest engagements, what they contain and their relative consequences.')


	with Data_Development:
		st.header('Data Development')
		st.write("Once the dataset was done and various cleaning and routine data manipulations have been done on python, I saved each tables, then deployed into PowerBi to have a good view of the datasets in powerquery and then exported it for visualization and insights drawing.")



	with visualization:
		st.header('Time to visualize our data!')
		st.write("#SentimentsAnalysis, #DataAnalysis, #Analysis, #Data, #DataVisualization, #PowerBi', #PythonAnalysis, #Python, #TwitterSentiments #Sentiments #Twitter, #TwitterInsights, #TwitterScrapper.")

		sel_col, disp_col = st.columns(2)

		#Dashboard = IFrame(src" ", width = 1000, height = 600)
		#display(Dashboard)

		img = Image.open("./image/6-a4.jpg")
		st.image(img)


	with inference:
		st.header("Insights")
		st.write("From our analysis, it could be noticed that in 2022 while the trend was at its peak, a certain user @mosyed110 letting out his disappointment at the news tweeted at around 11:45am on 30th Jan, 2022;'Imagine making it to ManUnited team, playing with players like Ronaldo at the age of 20, then f**cking it all up‚Ä¶ #greenwoodout', this tweet gathered the highest engagement which could be seen as wide acceptance and agreement from other users. In what looks like a tweet from a passionate fan, a  user, @obedient_dentist tweeted at around 5:27pm on the 3rd Feb, 2023;'Our rival club fans disguising themselves as ManU fans to say #greenwoodOUT.' It could be noted that users expressed both disappointments and encouragemnts to the issues on ground. This could also be seen as we have seen tweets where users stand in solidarity with the players and hopefully the team can be considerate enought to get him back and hopefully he regains his feet.")

		url = 'To view the interactive live dashboard on powerbi service, click  [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzdkNTdmNzItNTM3Yy00NTUzLWJkMWMtMDVhZGIzYTJjMWZjIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9)'
		st.markdown(url,unsafe_allow_html=True)

		urlp = 'To view my portfolio and contact me, please click  [Portfolio](https://letters-of-michael.github.io/Oluwaseyi-Michael.github.io/)'
		st.markdown(urlp,unsafe_allow_html=True)	

	with copywright:
		st.text('By Oluwaseyi Michael')




