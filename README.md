# playing-with-matches
Statistics project
CHEG 841
Random Phenomena
Graduate Project Proposal
Project Title: A Comparative Study Between a Predictive Regression Model and a Predictive Neural Network Applied to Grand Slam Tennis Matches
Group Members: Sai Praneet Batchu, Himaghna Bhattacharjee, Maximilian Cohen, Jon Wilson
Overview and Motivations
The goal of this project is to predict the winners and game differentials of the quarterfinal, semifinal, and final matches in a men’s singles grand slam tennis tournament based on the outcomes of the initial four rounds and player attributes. To make these predictions, we will use two different methods: a predictive regression model and a predictive neural network. We will rigorously develop these models and compare their accuracy. In our area of research, there is increasing interest in using large data sets to create predictive models to screen materials of interest. By identifying the key variables that predict the outcome of tennis tournaments and developing predictive tools, we hope to gain an understanding of the techniques necessary to develop models that identify key properties that can predict the performance of materials.
There are many features of tennis that make it an excellent sport for this kind of proposed statistical analysis. Like many sports, there is a large data set of relevant competition data, and we have found an online resource compiling tournament data for tennis from 1968 to 20151. In singles tennis, players compete in individual one-on-one matches, which eliminates the complexity of team dynamics and will make the analysis more tractable compared to other sports. We have chosen to focus on men’s tennis because they play the best of five sets as opposed to the best of three sets played by women. With more sets played, there will be more data available and single outlier rounds will make less of a difference in individual matches. We have chosen to focus on grand slam tournaments because traditionally the best players in the world will play in these tournaments and give their best effort in all their matches.
While there have been some prior works that utilize machine learning models to predict tennis matches, in each case we can identify significant differences between these studies and our proposed work. Therefore, we conclude our project would be unique. The most similar analysis was a study2 that identified 22 features and used historical data to train a neural network as well as a logistic regression model. Another analysis3 used similar inputs and trained their own logistic regression model. Our analysis will not use a logistic regression model because we will be predicting the continuous output of percentage of games won as opposed to a binary output of win/loss. Therefore, we recognize our proposed work as inherently different from these two papers. Some analyses4,5 discuss the effects of the serving and receiving abilities of a player and the nature of the court surface on the outcome, but they used a Markov model. Another6 discusses the effect of additional parameters such as fitness level, stamina and pressure handling capabilities of a player on the outcome, which is inherently different from our data inputs. One7 also attempts to quantify winning probabilities at a grand slam tournament, but it does so by predicting the outcome of every point played rather than looking at the match as a single output. An interesting study8 focused on identifying the important morphological characteristics that determine success in tennis players by using a machine learning algorithm. Their focus was to
improve the quality of training for Slovenian tennis players, so they did not study historical data. Our study will differ from the previous studies in that we will use the first half of a tournament to predict the results of the second half. We will use a combination of historical and morphological data to train and test a neural network and a regression model that will not be logistic. We will compare the two models, and to our knowledge, this analysis and comparison has not been performed with tennis data.
Analysis
Grand slam tournaments consist of seven single-elimination rounds, so we decided to use the first four rounds as input data for our model. We will use the players’ performance in the first four rounds of the tournament to predict the percentage of games each player will win in each of his matches in the final three rounds, and subsequently, who will win the matches of these rounds. To do this, we will use two different approaches both sourcing from the same input data and resulting in the same output metric. Of the past 47 years of data, we will use the data of four out of every five years to train our models and use the data of the fifth year to test the accuracy of our models. The first of our two models will be based on regression techniques. We will start with a basic linear equation in terms of our input parameters, and progressively add more complex functional forms of our inputs while maintaining tunable coefficients. Throughout the process, we will identify the important parameters and eliminate the negligible ones. The second of our two models will be a neural network. To avoid overfitting the data, we will first reduce the parameter space, and then we will generate the neural network. By using the testing data, we will obtain residuals of the two methods and quantify which is superior to the other. We will also look for opportunities to perform sensitivity analyses to determine the most important parameters and then compare which parameters are the most important to each model.
Some of the learning goals for the project are as follows:
1. Develop an understanding of creating a regression model
2. Develop an understanding of creating a neural network model
3. Learn about techniques to identify important parameters
4. Gain experience with the limitations of each of these types of models
Proposed Timeline
March:
• Compile the data into an appropriate format to be accessed by Python
• Meet with the course consultant to ensure our approach is appropriate
April:
• Complete analysis by fully developing both models from the training data
• Test robustness of the predictions on data from the testing data
• Begin writing final report
May:
• Complete and submit final report
• Create a presentation and give it to the class
References
1. https://github.com/JeffSackmann/tennis_atp
2. Michal Sipko. Machine Learning for the Prediction of Professional Tennis Matches“. MA thesis. Imperial College London, 2015.
3. Shang-Min Ma , Chao-Chin Liu , Yue Tan & Shang-Chun Ma (2013). Winning matches in Grand Slam Men's Singles: An analysis of player performance-related variables from 1991 to 2008, Journal of Sports Sciences, 31:11, 1147-1155, DOI: 10.1080/02640414.2013.775472
4. http://thesportsquotient.com/tennis/2016/11/7/statistical-modeling-of-atp-singles-matches-part-ii.
5. Knottenbelt W.J. et al., A common-opponent stochastic model for predicting the outcome of professional tennis matches, Computers and Mathematics with Applications 64 (2012) 3820–3827.
6. http://www.abc.net.au/news/science/2018-01-16/australian-open-tennis-statistics-clutch-time-pressure-work-win/9329322.
7. O'Malley, A. (2008). Probability Formulas and Statistical Analysis in Tennis. Journal of Quantitative Analysis in Sports, 4(2), pp. -. Retrieved 23 Feb. 2018, from doi:10.2202/1559-0410.1100. 8. Panjan A, Sarabon N, Filipčič A. Prediction of the successfulness of tennis players with machine learning methods. Kinesiology. 2010;42(1): 98–106.